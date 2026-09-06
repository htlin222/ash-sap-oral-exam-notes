# ASH-SAP 血液科口試問答筆記

依據《American Society of Hematology Self-Assessment Program, 9th Edition (2025)》（ASH-SAP 9e）改寫的血液科專科口試準備筆記。格式為「編號問題 + 條列重點回答」，以口試委員提問的角度整理重點，全書 49 章。

僅供個人讀書與考試準備使用，非商業用途。內容經過改寫與濃縮，若與原著或最新臨床指引有出入，請以原書與最新文獻為準，不作為臨床決策依據。

## 內容來源（唯一真實來源）

所有輸出格式都是從 [`converted/`](./converted) 底下的 49 個 `.md` 檔案自動產生的。要更新內容，直接編輯這些 markdown 檔案即可；其他所有格式（EPUB、PDF、Anki、網站、影片）都會在 CI 中自動重新建置。

## 輸出格式

| 格式 | 說明 | 產生方式 |
| --- | --- | --- |
| **EPUB** | 極簡黑白樣式，Kindle 相容（可透過 Send-to-Kindle 或直接匯入） | [`epub-build/build.sh`](./epub-build/build.sh)，需要 `pandoc` |
| **PDF** | 極簡黑白版面，A5 尺寸 | [`pdf-build/build.sh`](./pdf-build/build.sh)，需要 `pandoc` + `weasyprint` |
| **Anki 卡包** | 單一 `.apkg`，牌組結構 `血專口試::章節`，共約 2500+ 張卡 | [`anki-build/build_anki.py`](./anki-build/build_anki.py)，需要 `pandoc`，用 `uv run` 執行 |
| **網站** | Astro Starlight 文件網站，逐章可搜尋瀏覽 | [`site/`](./site)，`npm run build` |
| **章節影片** | 16:9，每章一支，靜態黑白極簡投影片 + `zh-TW-YunJheNeural` 語音旁白逐題朗讀 | [`video-build/make_chapter_video.py`](./video-build/make_chapter_video.py)，需要 `pandoc` + `ffmpeg` + ImageMagick，用 `uv run` 執行 |

`converted/**.md` 有異動並 push 到 `main` 時，GitHub Actions 會自動：

1. 重新建置 EPUB + PDF + Anki 卡包，並發布為 [GitHub Release](../../releases)（版本化 tag，每次建置一個新 release）。
2. 重新建置並部署 Starlight 網站到 GitHub Pages。
3. 重新產生有異動章節的影片，全部上傳到同一個 [`videos-final`](../../releases/tag/videos-final) GitHub Release（49 章平行處理，見 [`release-videos.yml`](./.github/workflows/release-videos.yml)）。

## 本機建置

```bash
# EPUB
cd epub-build && ./build.sh

# PDF（需要 pandoc + weasyprint）
cd pdf-build && ./build.sh

# Anki 卡包（需要 uv；會自動安裝 genanki / beautifulsoup4）
cd anki-build && uv run build_anki.py

# 網站（本機預覽）
cd site && npm install && npm run dev

# 單一章節影片（需要 pandoc + ffmpeg + ImageMagick；用 uv 執行）
cd video-build && uv run make_chapter_video.py ../converted/01-*.md -o out/01.mp4
```

## 目錄結構

```
converted/       # 49 章節 markdown（唯一內容來源）
epub-build/      # EPUB 樣式 + 建置腳本
pdf-build/       # PDF 樣式 + 建置腳本
anki-build/      # Anki 卡包產生腳本
site/            # Astro Starlight 文件網站
video-build/     # 章節影片產生腳本（投影片 + TTS + ffmpeg 串接）
.github/workflows/
  release.yml         # converted/**.md 變動 -> 建置 + 發布 EPUB/PDF
  deploy-site.yml     # converted/**.md 變動 -> 建置 + 部署網站
  release-videos.yml  # converted/**.md 變動 -> 平行產生章節影片 + 發布
```
