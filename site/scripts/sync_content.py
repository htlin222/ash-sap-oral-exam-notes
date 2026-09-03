#!/usr/bin/env python3
"""
把 ../converted/*.md（ASH-SAP 口試問答筆記，唯一內容來源）同步進
src/content/docs/chapters/，轉成 Starlight 看得懂的格式（加上
frontmatter，並移除內文重複的 H1，因為 Starlight 會用 frontmatter
的 title 自動渲染標題）。

在 npm run dev / npm run build 前會自動執行（見 package.json 的
predev / prebuild）。也可以手動執行：
    python3 scripts/sync_content.py
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONVERTED_DIR = ROOT.parent / "converted"
CHAPTERS_DIR = ROOT / "src" / "content" / "docs" / "chapters"


def yaml_escape(text: str) -> str:
    return text.replace('"', '\\"')


def extract_title_and_body(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    title = "未命名章節"
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            body_start = i + 1
            break
    body = "\n".join(lines[body_start:]).lstrip("\n")
    return title, body


def sync() -> None:
    if CHAPTERS_DIR.exists():
        shutil.rmtree(CHAPTERS_DIR)
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(CONVERTED_DIR.glob("*.md"))
    if not md_files:
        raise SystemExit(f"找不到來源 markdown：{CONVERTED_DIR}")

    for src in md_files:
        text = src.read_text(encoding="utf-8")
        title, body = extract_title_and_body(text)

        m = re.match(r"^(\d+)-", src.stem)
        order = int(m.group(1)) if m else 0

        frontmatter = (
            "---\n"
            f'title: "{yaml_escape(title)}"\n'
            f"sidebar:\n"
            f"  order: {order}\n"
            "---\n\n"
        )

        dest = CHAPTERS_DIR / src.name
        dest.write_text(frontmatter + body, encoding="utf-8")

    print(f"已同步 {len(md_files)} 個章節到 {CHAPTERS_DIR}")


if __name__ == "__main__":
    sync()
