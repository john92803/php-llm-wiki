#!/usr/bin/env python3
"""把 wiki/ 轉成 GitHub Wiki 格式（輸出到 .cache/github-wiki/，或 --out 指定目錄）。

GitHub Wiki 的差異與對應：
  - 所有頁面在同一層、用檔名當頁名 → concepts/php-tags.md 變成頁面 php-tags
  - [[slug]] 是 GitHub Wiki 原生語法，會連到同名頁面 → 保留不動
  - 首頁必須叫 Home.md → 由 wiki/index.md 轉成，相對連結改成頁名
  - frontmatter 不會被渲染 → 轉成表格
  - 另外產生 _Sidebar.md（導覽）、_Footer.md（說明來源）、Workflow.md（docs/workflow.md）

wiki/ 仍是唯一的編輯來源；GitHub Wiki 是發佈出來的副本，不要直接在網頁上改。
用法：python3 tools/build_github_wiki.py [--out DIR]
"""
import argparse
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
REPO_URL = "https://github.com/john92803/php-llm-wiki"

FIELD_NAMES = {
    "id": "ID", "title": "標題", "slug": "slug", "raw": "原文", "subpages": "子頁面",
    "fidelity": "fidelity", "ingested": "ingest 日期", "sources": "出處", "related": "相關",
}


def page_link(m: re.Match) -> str:
    """[text](concepts/php-tags.md) → [text](php-tags)"""
    text, target = m.group(1), m.group(2)
    if target.endswith(".md") and "://" not in target:
        name = pathlib.Path(target).stem
        if text.endswith(".md"):
            text = name
        return f"[{text}]({name})"
    return m.group(0)


def convert(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if m:
        rows = ["| 欄位 | 值 |", "|---|---|"]
        for line in m.group(1).splitlines():
            if ":" not in line:
                continue
            k, v = (s.strip() for s in line.split(":", 1))
            if k == "raw":
                v = f"[{v}]({REPO_URL}/blob/main/{v})"
            rows.append(f"| {FIELD_NAMES.get(k, k)} | {v} |")
        text = "\n".join(rows) + "\n\n" + text[m.end():]
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", page_link, text)
    # 讓標題層級從 ## 開始的頁面也有一個 H1 以外的清楚結構：GitHub Wiki 會用頁名當 H1
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / ".cache" / "github-wiki"))
    out = pathlib.Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    # 只清掉 .md（保留 .git，讓這個目錄可以直接是 wiki repo 的 clone）
    for f in out.glob("*.md"):
        f.unlink()

    pages = sorted((WIKI / "concepts").glob("*.md")) + sorted((WIKI / "sources").glob("*.md"))
    for p in pages:
        (out / p.name).write_text(convert(p.read_text(encoding="utf-8")), encoding="utf-8")

    index = convert((WIKI / "index.md").read_text(encoding="utf-8"))
    index = index.replace("# Wiki 目錄", "# PHP 語言基礎 LLM Wiki", 1)
    intro = (
        "以 PHP 官方中文手冊（基本語法、類型、變數、常數、表達式）為來源，"
        "寫給「寫過 Python／C／JavaScript、沒碰過 PHP」的讀者。每一句知識都附出處 ID（例如 `[S2.4]`），"
        f"可以追回 repo 裡的 [raw/]({REPO_URL}/tree/main/raw) 原文。\n\n"
        f"- 教學簡報：[slides/index.html]({REPO_URL}/blob/main/slides/index.html)（下載後用瀏覽器開啟）\n"
        "- 流程設計與反思：[Workflow](Workflow)\n"
        "- 操作紀錄：[log](log)\n"
    )
    index = index.replace("> 每頁一行摘要。新增頁面時同步更新。", intro, 1)
    (out / "Home.md").write_text(index, encoding="utf-8")

    (out / "log.md").write_text(convert((WIKI / "log.md").read_text(encoding="utf-8")), encoding="utf-8")

    wf = (ROOT / "docs" / "workflow.md").read_text(encoding="utf-8")
    wf = re.sub(r"\]\((?!https?://)([^)]+)\)", lambda m: f"]({REPO_URL}/blob/main/docs/{m.group(1)})", wf)
    (out / "Workflow.md").write_text(wf, encoding="utf-8")

    # 側邊欄：從 index 的分類與連結產生
    side = ["**[首頁](Home)**", ""]
    for line in index.splitlines():
        if line.startswith("## ") or line.startswith("### "):
            side += ["", f"**{line.lstrip('# ').strip()}**", ""]
        m = re.match(r"- \[[^\]]+\]\(([^)]+)\) — (.*)", line)
        if m:
            name = m.group(1)
            side.append(f"- [{name}]({name})")
    side += ["", "**其他**", "", "- [Workflow](Workflow)", "- [log](log)"]
    (out / "_Sidebar.md").write_text("\n".join(side) + "\n", encoding="utf-8")
    (out / "_Footer.md").write_text(
        f"本 Wiki 由 [`tools/build_github_wiki.py`]({REPO_URL}/blob/main/tools/build_github_wiki.py) "
        "從 repo 的 `wiki/` 產生；請在 repo 修改後重新發佈，不要直接在網頁上編輯。\n",
        encoding="utf-8",
    )
    print(f"wrote {len(list(out.glob('*.md')))} pages to {out}")


if __name__ == "__main__":
    main()
