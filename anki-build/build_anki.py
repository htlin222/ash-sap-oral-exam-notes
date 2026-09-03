#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "genanki>=0.13",
#     "beautifulsoup4>=4.12",
# ]
# ///
"""
把 converted/*.md（ASH-SAP 口試問答筆記）轉成單一 Anki .apkg 卡包。

用法：
    uv run build_anki.py
    uv run build_anki.py --input ../converted --output ../ash-sap-oral-exam.apkg

需要系統已安裝 pandoc（用來把 markdown 正確轉成 HTML，特別是巢狀清單/表格）。

可以重複執行：牌組/筆記 ID 皆由名稱/內容做 deterministic hash，
重新產生的 .apkg 匯入 Anki 後會對應到同一組牌組與筆記（而不是重複建立）。
每次來源 markdown 更新後，重跑本腳本即可得到最新的 .apkg。
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

import genanki
from bs4 import BeautifulSoup, NavigableString, Tag


def markdown_to_html(text: str) -> str:
    """Convert markdown to HTML via pandoc (correctly handles 3-space nested
    lists/tables under numbered items, which python-markdown mishandles)."""
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

TOP_DECK_NAME = "血專口試"

CSS = """
.card {
  font-family: -apple-system, "PingFang TC", "Noto Sans CJK TC", "Microsoft JhengHei", serif;
  font-size: 18px;
  color: #000000;
  background-color: #ffffff;
  text-align: left;
  line-height: 1.5;
  padding: 0.5em 0.8em;
}
.chapter-tag {
  font-size: 0.75em;
  color: #555555;
  border-bottom: 1px solid #cccccc;
  margin-bottom: 0.6em;
  padding-bottom: 0.3em;
}
.question {
  font-weight: bold;
  font-size: 1.05em;
}
hr#answer {
  border: none;
  border-top: 1px solid #000000;
  margin: 0.9em 0;
}
.answer ul, .answer ol {
  margin: 0.3em 0;
  padding-left: 1.3em;
}
.answer li {
  margin: 0.35em 0;
}
.answer table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.6em 0;
  font-size: 0.85em;
}
.answer th, .answer td {
  border: 1px solid #000000;
  padding: 0.3em 0.4em;
  text-align: left;
  vertical-align: top;
}
.answer th {
  border-bottom: 2px solid #000000;
}
.answer strong { font-weight: bold; }
.answer em { font-style: italic; }
"""

QFMT = """
<div class="chapter-tag">{{Chapter}} · {{Section}}</div>
<div class="question">{{Question}}</div>
"""

AFMT = """
{{FrontSide}}
<hr id="answer">
<div class="answer">{{Answer}}</div>
"""


def stable_id(*parts: str) -> int:
    """Deterministic positive int ID for genanki Deck/Model, derived from name."""
    digest = hashlib.sha256("::".join(parts).encode("utf-8")).hexdigest()
    return (int(digest[:12], 16) % (1 << 31)) + (1 << 30)


def make_model() -> genanki.Model:
    return genanki.Model(
        stable_id("model", "ash-sap-oral-exam-v1"),
        "ASH-SAP 口試問答",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
            {"name": "Chapter"},
            {"name": "Section"},
        ],
        templates=[
            {
                "name": "問答卡",
                "qfmt": QFMT,
                "afmt": AFMT,
            }
        ],
        css=CSS,
    )


def slugify_tag(text: str) -> str:
    text = re.sub(r"[()（）「」『』,、·:：;；\s]+", "_", text.strip())
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "misc"


def extract_h1_title(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            title = re.sub(r"^Chapter\s+\d+\s*[:：]\s*", "", title)
            return title
    return "未命名章節"


def li_to_question_answer(li: Tag) -> tuple[str, str]:
    """Split a <li> (one numbered Q&A item) into (question_html, answer_html)."""
    contents = list(li.contents)
    if not contents:
        return "", ""

    first = contents[0]
    if isinstance(first, Tag) and first.name == "p":
        question_html = first.decode_contents().strip()
        rest = contents[1:]
    else:
        # Tight list item: leading text node(s) up to the first block-level tag.
        q_parts = []
        idx = 0
        for idx, node in enumerate(contents):
            if isinstance(node, Tag) and node.name in ("ul", "ol", "table", "p", "blockquote"):
                break
            q_parts.append(str(node))
        else:
            idx = len(contents)
        question_html = "".join(q_parts).strip()
        rest = contents[idx:]

    answer_html = "".join(
        str(node) for node in rest
    ).strip()
    return question_html, answer_html


def chapter_to_notes(model: genanki.Model, md_path: Path) -> tuple[str, list[genanki.Note]]:
    text = md_path.read_text(encoding="utf-8")
    title = extract_h1_title(text)

    html = markdown_to_html(text)
    soup = BeautifulSoup(html, "html.parser")

    notes: list[genanki.Note] = []
    current_section = ""

    for node in list(soup.contents):
        if isinstance(node, NavigableString):
            continue
        if node.name in ("h2", "h3"):
            current_section = node.get_text().strip()
        elif node.name == "ol":
            for li in node.find_all("li", recursive=False):
                q_html, a_html = li_to_question_answer(li)
                if not q_html:
                    continue
                note = genanki.Note(
                    model=model,
                    fields=[q_html, a_html, title, current_section],
                    tags=[
                        "ash-sap",
                        f"chapter::{slugify_tag(title)}",
                        f"section::{slugify_tag(current_section)}",
                    ],
                )
                notes.append(note)

    return title, notes


def build(input_dir: Path, output_path: Path) -> None:
    if shutil.which("pandoc") is None:
        sys.exit("需要 pandoc（用於 markdown -> HTML 轉換），請先安裝：brew install pandoc")

    model = make_model()
    top_deck_id = stable_id("deck", TOP_DECK_NAME)
    # A visible top-level deck so importing always creates/updates 血專口試 itself too.
    top_deck = genanki.Deck(top_deck_id, TOP_DECK_NAME)

    decks: list[genanki.Deck] = [top_deck]
    total_notes = 0

    md_files = sorted(input_dir.glob("*.md"))
    if not md_files:
        raise SystemExit(f"找不到任何 .md 檔案於 {input_dir}")

    for md_path in md_files:
        m = re.match(r"^(\d+)-", md_path.stem)
        num = int(m.group(1)) if m else 0

        title, notes = chapter_to_notes(model, md_path)
        if not notes:
            print(f"[skip] {md_path.name}: 沒有解析到任何問答")
            continue

        deck_name = f"{TOP_DECK_NAME}::{num:02d} {title}"
        deck = genanki.Deck(stable_id("deck", deck_name), deck_name)
        for note in notes:
            deck.add_note(note)
        decks.append(deck)
        total_notes += len(notes)
        print(f"[ok] {md_path.name}: {len(notes)} 題 -> {deck_name}")

    package = genanki.Package(decks)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    package.write_to_file(str(output_path))
    print(f"\n完成：共 {len(decks) - 1} 個章節牌組、{total_notes} 張卡片")
    print(f"輸出：{output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "converted",
        help="來源 markdown 資料夾（預設：../converted）",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent / f"{TOP_DECK_NAME}.apkg",
        help="輸出 .apkg 路徑",
    )
    args = parser.parse_args()
    build(args.input, args.output)


if __name__ == "__main__":
    main()
