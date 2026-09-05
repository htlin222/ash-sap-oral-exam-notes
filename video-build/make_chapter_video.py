#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "edge-tts>=6.1",
#     "beautifulsoup4>=4.12",
# ]
# ///
"""
把一章 converted/*.md 轉成一支 16:9 影片：逐題「靜態投影片 + 語音旁白」
產生 clip，再串接成一支章節影片。刻意不做動畫效果 —— 只借用「文字卡 ->
TTS -> 合成 -> 串接」這個流程,風格維持黑白極簡（跟 EPUB/PDF/網站一致）。

用法：
    uv run make_chapter_video.py ../converted/01-....md -o out/01-....mp4
    uv run make_chapter_video.py ../converted/01-....md -o out/01-....mp4 --voice zh-TW-YunJheNeural

需要系統已安裝：pandoc、ImageMagick（magick）、ffmpeg。
"""

from __future__ import annotations

import argparse
import asyncio
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import edge_tts
from bs4 import BeautifulSoup, NavigableString, Tag

WIDTH = 1920
HEIGHT = 1080
FPS = 30

ACCENT = "#9a2f2f"
BLACK = "#000000"
WHITE = "#ffffff"
GRAY = "#555555"

FONT_CJK_BOLD_CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
]
FONT_CJK_REGULAR_CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
]


def first_existing(paths: list[str]) -> str:
    for p in paths:
        if Path(p).exists():
            return p
    raise SystemExit(f"找不到可用字型，試過：{paths}")


def check_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"需要系統指令 `{name}`，請先安裝。")


# ImageMagick 7 用 `magick`；Ubuntu 上常見還是 IM6，只有 `convert`。兩者的
# 基本單指令用法（無 magick 子命令）相容，挑有的那個即可。
MAGICK_BIN = "magick" if shutil.which("magick") else "convert"


def markdown_to_html(text: str) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html", "--wrap=none"],
        input=text,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc 轉換失敗: {result.stderr}")
    return result.stdout


def im_escape(s: str) -> str:
    """ImageMagick's caption:/label:/-annotate text interprets `%` escape
    sequences (e.g. %d, %f, %w) — very common in our content ("50%..."),
    and left unescaped it silently corrupts/duplicates the rendered text.
    Doubling `%` -> `%%` renders a literal percent sign instead."""
    return s.replace("%", "%%")


def clean_text(s: str) -> str:
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{2,}", "\n", s)
    return s.strip()


def li_to_question_answer(li: Tag) -> tuple[str, str]:
    """把一個 <li>（一題問答）拆成 (question_text, answer_text)，純文字。"""
    contents = list(li.contents)
    if not contents:
        return "", ""

    first = contents[0]
    if isinstance(first, Tag) and first.name == "p":
        question = first.get_text(" ", strip=True)
        rest = contents[1:]
    else:
        parts = []
        idx = 0
        for idx, node in enumerate(contents):
            if isinstance(node, Tag) and node.name in ("ul", "ol", "table", "p", "blockquote"):
                break
            parts.append(str(node) if isinstance(node, NavigableString) else node.get_text())
        else:
            idx = len(contents)
        question = "".join(parts).strip()
        rest = contents[idx:]

    answer_parts: list[str] = []
    for node in rest:
        if isinstance(node, NavigableString):
            t = str(node).strip()
            if t:
                answer_parts.append(t)
            continue
        if not isinstance(node, Tag):
            continue
        if node.name == "table":
            rows = node.find_all("tr")
            for row in rows:
                cells = [c.get_text(" ", strip=True) for c in row.find_all(["th", "td"])]
                cells = [c for c in cells if c]
                if cells:
                    answer_parts.append("；".join(cells))
        elif node.name in ("ul", "ol"):
            for li_item in node.find_all("li", recursive=False):
                t = li_item.get_text(" ", strip=True)
                if t:
                    answer_parts.append(t)
        else:
            t = node.get_text(" ", strip=True)
            if t:
                answer_parts.append(t)

    return clean_text(question), "\n".join(answer_parts)


def extract_h1_title(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            title = re.sub(r"^Chapter\s+\d+\s*[:：]\s*", "", title)
            return title
    return "未命名章節"


def parse_chapter(md_path: Path) -> tuple[str, list[tuple[str, str]]]:
    text = md_path.read_text(encoding="utf-8")
    title = extract_h1_title(text)
    html = markdown_to_html(text)
    soup = BeautifulSoup(html, "html.parser")

    qa_pairs: list[tuple[str, str]] = []
    for node in list(soup.contents):
        if not isinstance(node, Tag):
            continue
        if node.name == "ol":
            for li in node.find_all("li", recursive=False):
                q, a = li_to_question_answer(li)
                if q:
                    qa_pairs.append((q, a))
    return title, qa_pairs


# ---------------------------------------------------------------------------
# TTS
# ---------------------------------------------------------------------------


async def synth(text: str, voice: str, rate: str, out_path: Path, attempts: int = 3) -> None:
    last_err: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            communicate = edge_tts.Communicate(text, voice, rate=rate)
            await communicate.save(str(out_path))
            if out_path.stat().st_size > 0:
                return
            raise RuntimeError("empty audio output")
        except Exception as e:  # noqa: BLE001
            last_err = e
            print(f"  TTS attempt {attempt}/{attempts} failed: {e}", file=sys.stderr)
            if attempt < attempts:
                await asyncio.sleep(attempt * 3)
    raise RuntimeError(f"TTS 失敗（{attempts} 次）: {last_err}")


# ---------------------------------------------------------------------------
# Slide rendering (ImageMagick) — 黑白極簡 + 單一暗紅強調色
# ---------------------------------------------------------------------------


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(result.stderr.decode("utf-8", errors="replace"), file=sys.stderr)
        raise subprocess.CalledProcessError(result.returncode, cmd)


def render_slide(
    out_png: Path,
    header: str,
    question: str,
    answer: str,
    font_bold: str,
    font_regular: str,
) -> None:
    tmp = out_png.parent
    header_png = tmp / f"{out_png.stem}-header.png"
    question_png = tmp / f"{out_png.stem}-question.png"
    answer_png = tmp / f"{out_png.stem}-answer.png"
    divider_png = tmp / f"{out_png.stem}-divider.png"

    header_h = 90
    question_h = 330
    divider_h = 6
    answer_h = HEIGHT - header_h - question_h - divider_h

    run([
        MAGICK_BIN, "-size", f"{WIDTH}x{header_h}", f"xc:{WHITE}",
        "-font", font_regular, "-pointsize", "34", "-fill", ACCENT,
        "-gravity", "West", "-annotate", "+60+0", im_escape(header),
        header_png.as_posix(),
    ])
    run([
        MAGICK_BIN, "-size", f"{WIDTH}x{divider_h}", f"xc:{BLACK}",
        divider_png.as_posix(),
    ])
    inner_w = WIDTH - 160
    run([
        MAGICK_BIN, "-size", f"{inner_w}x{question_h}", "-background", WHITE,
        "-font", font_bold, "-fill", BLACK, "-gravity", "Center",
        f"caption:{im_escape(question)}",
        "-gravity", "center", "-background", WHITE, "-extent", f"{WIDTH}x{question_h}",
        question_png.as_posix(),
    ])
    if answer:
        inner_w2 = WIDTH - 200
        run([
            MAGICK_BIN, "-size", f"{inner_w2}x{answer_h}", "-background", WHITE,
            "-font", font_regular, "-fill", GRAY, "-gravity", "North",
            f"caption:{im_escape(answer)}",
            "-gravity", "north", "-background", WHITE, "-extent", f"{WIDTH}x{answer_h}",
            answer_png.as_posix(),
        ])
    else:
        run([MAGICK_BIN, "-size", f"{WIDTH}x{answer_h}", f"xc:{WHITE}", answer_png.as_posix()])
    run([
        MAGICK_BIN,
        header_png.as_posix(), divider_png.as_posix(),
        question_png.as_posix(), answer_png.as_posix(),
        "-append",
        out_png.as_posix(),
    ])
    for p in (header_png, question_png, answer_png, divider_png):
        p.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# Clip assembly (ffmpeg)
# ---------------------------------------------------------------------------


def make_clip(image: Path, audio: Path, out_mp4: Path) -> None:
    run([
        "ffmpeg", "-y", "-loop", "1", "-i", image.as_posix(),
        "-i", audio.as_posix(),
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p", "-r", str(FPS), "-vf", f"scale={WIDTH}:{HEIGHT}",
        "-shortest",
        out_mp4.as_posix(),
    ])


def concat_clips(clips: list[Path], out_mp4: Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        for c in clips:
            f.write(f"file '{c.resolve().as_posix()}'\n")
        list_path = Path(f.name)
    try:
        run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_path.as_posix(),
            "-c", "copy",
            out_mp4.as_posix(),
        ])
    finally:
        list_path.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


async def build_chapter_video(
    md_path: Path,
    out_path: Path,
    voice: str,
    rate: str,
    work_dir: Path,
    only: int | None = None,
) -> None:
    check_tool("pandoc")
    check_tool(MAGICK_BIN)
    check_tool("ffmpeg")

    font_bold = first_existing(FONT_CJK_BOLD_CANDIDATES)
    font_regular = first_existing(FONT_CJK_REGULAR_CANDIDATES)

    title, qa_pairs = parse_chapter(md_path)
    if only:
        qa_pairs = qa_pairs[:only]
    print(f"章節：{title}（{len(qa_pairs)} 題）")

    work_dir.mkdir(parents=True, exist_ok=True)
    clip_paths: list[Path] = []

    # Clip 0：章節標題頁
    intro_audio = work_dir / "clip-000.mp3"
    intro_png = work_dir / "clip-000.png"
    intro_mp4 = work_dir / "clip-000.mp4"
    await synth(f"{title}。", voice, rate, intro_audio)
    render_slide(
        intro_png,
        header="ASH-SAP 血液科口試問答筆記",
        question=title,
        answer="",
        font_bold=font_bold,
        font_regular=font_regular,
    )
    make_clip(intro_png, intro_audio, intro_mp4)
    clip_paths.append(intro_mp4)

    for i, (question, answer) in enumerate(qa_pairs, start=1):
        print(f"  [{i}/{len(qa_pairs)}] {question[:40]}...")
        audio_path = work_dir / f"clip-{i:03d}.mp3"
        png_path = work_dir / f"clip-{i:03d}.png"
        mp4_path = work_dir / f"clip-{i:03d}.mp4"

        narration = f"第 {i} 題。{question}{answer.replace(chr(10), '，')}"
        await synth(narration, voice, rate, audio_path)
        render_slide(
            png_path,
            header=f"{title}　·　Q{i}",
            question=question,
            answer=answer,
            font_bold=font_bold,
            font_regular=font_regular,
        )
        make_clip(png_path, audio_path, mp4_path)
        clip_paths.append(mp4_path)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    concat_clips(clip_paths, out_path)
    print(f"完成：{out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path, help="來源章節 markdown 檔")
    parser.add_argument("-o", "--output", type=Path, required=True, help="輸出 mp4 路徑")
    parser.add_argument("--voice", default="zh-TW-YunJheNeural", help="edge-tts 語音")
    parser.add_argument("--rate", default="+0%", help="edge-tts 語速調整")
    parser.add_argument("--work-dir", type=Path, default=None, help="暫存資料夾（預設用系統暫存目錄）")
    parser.add_argument("--only", type=int, default=None, help="只處理前 N 題（測試用）")
    parser.add_argument("--keep-work-dir", action="store_true", help="保留暫存 clip 檔案（除錯用）")
    args = parser.parse_args()

    work_dir = args.work_dir or Path(tempfile.mkdtemp(prefix="ash-sap-video-"))
    try:
        asyncio.run(
            build_chapter_video(
                args.markdown, args.output, args.voice, args.rate, work_dir, args.only
            )
        )
    finally:
        if not args.keep_work_dir and args.work_dir is None:
            shutil.rmtree(work_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
