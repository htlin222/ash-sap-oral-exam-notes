#!/usr/bin/env bash
# 產生極簡黑白 PDF：pandoc (md -> standalone HTML) -> weasyprint (HTML -> PDF)
# 用法: ./build.sh [輸出路徑]
set -euo pipefail

cd "$(dirname "$0")"

OUT="${1:-../ash-sap-oral-exam-notes.pdf}"
CONVERTED_DIR="../converted"
HTML_TMP="$(mktemp -t ash-sap-pdf-XXXX).html"

pandoc ../epub-build/metadata.yaml ../epub-build/00-preface.md "$CONVERTED_DIR"/*.md \
  -o "$HTML_TMP" \
  --standalone \
  --toc --toc-depth=1 --metadata=toc-title:"目錄" \
  --css="$(pwd)/print.css" \
  --to=html5

if command -v weasyprint >/dev/null 2>&1; then
  weasyprint "$HTML_TMP" "$OUT"
else
  python3 -m weasyprint "$HTML_TMP" "$OUT"
fi

rm -f "$HTML_TMP"
echo "PDF 已產生: $OUT"
