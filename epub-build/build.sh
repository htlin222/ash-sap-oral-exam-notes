#!/usr/bin/env bash
# 產生極簡黑白、Kindle 相容的 EPUB。
# 用法: ./build.sh [輸出路徑]
set -euo pipefail

cd "$(dirname "$0")"

OUT="${1:-../ash-sap-oral-exam-notes.epub}"
CONVERTED_DIR="../converted"

pandoc metadata.yaml 00-preface.md "$CONVERTED_DIR"/*.md \
  -o "$OUT" \
  --toc --toc-depth=1 \
  --split-level=1 \
  --css=style.css \
  --epub-cover-image=cover.png \
  --standalone

echo "EPUB 已產生: $OUT"
