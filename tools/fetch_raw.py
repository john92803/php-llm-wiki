#!/usr/bin/env python3
"""fetch 節點：下載 PHP 官方手冊子頁面，逐字擷取正文寫入 raw/。

做法（對應 CLAUDE.md §4 資料可信度規則）：
  1. 只抓子頁面（pages.tsv 列出的 20 頁），不從章節目錄頁擷取知識。
  2. 用 curl 下載原始 HTML（不經過會摘要的 WebFetch），所以內容是逐字的。
  3. 只取 <div id="頁面ID"> 正文；<section id="usernotes">（User Contributed Notes）
     在正文 div 之外，天然被排除，另外再檢查一次。
  4. 程式碼區塊轉成 ```php 圍欄，其餘用 pandoc 轉成 GFM。
  5. raw/ 已存在就不覆寫（immutable）；要補內容請另外新增段落並寫 log。

用法：python3 tools/fetch_raw.py [--html-dir DIR]
"""
import argparse
import datetime
import pathlib
import subprocess
import sys

from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://www.php.net/manual/zh/{}.php"

SOURCES = {
    "S1": ("01-basic-syntax.md", "基本語法", "language.basic-syntax"),
    "S2": ("02-types.md", "類型", "language.types"),
    "S3": ("03-variables.md", "變數", "language.variables"),
    "S4": ("04-constants.md", "常數", "language.constants"),
    "S5": ("05-expressions.md", "表達式", "language.expressions"),
}

PAGES = [
    ("S1.1", "language.basic-syntax.phptags", "PHP 標記"),
    ("S1.2", "language.basic-syntax.phpmode", "從 HTML 中分離"),
    ("S1.3", "language.basic-syntax.instruction-separation", "指令分隔符"),
    ("S1.4", "language.basic-syntax.comments", "註解"),
    ("S2.1", "language.types.intro", "簡介"),
    ("S2.2", "language.types.type-system", "型別系統"),
    ("S2.3", "language.types.null", "NULL"),
    ("S2.4", "language.types.boolean", "Boolean"),
    ("S2.5", "language.types.integer", "Integer"),
    ("S2.6", "language.types.float", "Float"),
    ("S2.7", "language.types.string", "String"),
    ("S2.8", "language.types.array", "Array"),
    ("S2.9", "language.types.type-juggling", "型別轉換"),
    ("S3.1", "language.variables.basics", "基礎"),
    ("S3.2", "language.variables.scope", "作用域"),
    ("S3.3", "language.variables.variable", "可變變數"),
    ("S3.4", "language.variables.predefined", "預定義變數"),
    ("S4.1", "language.constants.syntax", "語法"),
    ("S4.2", "language.constants.magic", "魔術常數"),
    ("S5.1", "language.expressions", "表達式"),
]


def download(page: str, html_dir: pathlib.Path) -> pathlib.Path:
    path = html_dir / f"{page}.html"
    if not path.exists():
        subprocess.run(["curl", "-sS", "-f", "-o", str(path), BASE.format(page)], check=True)
    return path


def extract(page: str, html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    body = soup.find(id=page)
    if body is None:
        raise SystemExit(f"{page}: 找不到正文 div#{page}")
    if body.find(id="usernotes"):
        raise SystemExit(f"{page}: 正文裡混入 usernotes，停止")
    # 程式碼：保留純文字，改成 <pre><code class="php">，pandoc 會轉成 ```php
    for div in body.select("div.phpcode"):
        pre = soup.new_tag("pre")
        code = soup.new_tag("code", attrs={"class": "php"})
        code.string = div.get_text()
        pre.append(code)
        div.replace_with(pre)
    # 連結只留文字，避免相對網址失效
    for a in body.find_all("a"):
        a.unwrap()
    md = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
        input=str(body), capture_output=True, text=True, check=True,
    ).stdout
    return md.strip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-dir", default=str(ROOT / ".cache" / "html"))
    args = ap.parse_args()
    html_dir = pathlib.Path(args.html_dir)
    html_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()
    raw = ROOT / "raw"
    raw.mkdir(exist_ok=True)

    for sid, (fname, title, chapter) in SOURCES.items():
        out = raw / fname
        if out.exists():
            print(f"skip {out.name}（raw/ 不可修改）")
            continue
        parts = [
            f"# {sid} {title}（raw）\n",
            f"- 章節：`{chapter}`",
            f"- 取得方式：curl 下載 {BASE.format('<頁面>')} 原始 HTML → 擷取 `div#<頁面ID>` 正文"
            " → 排除 User Contributed Notes → pandoc 轉 Markdown（tools/fetch_raw.py）",
            f"- 抓取日期：{today}",
            "- 本檔為官方手冊原文（簡體中文），不可修改。\n",
        ]
        for pid, page, ptitle in PAGES:
            if not pid.startswith(sid + "."):
                continue
            html = download(page, html_dir).read_text(encoding="utf-8")
            body = extract(page, html)
            parts.append(f"---\n\n## [{pid}] {ptitle}\n")
            parts.append(f"- url: {BASE.format(page)}")
            parts.append("- fidelity: verbatim")
            parts.append(f"- fetched: {today}\n")
            parts.append(body)
        out.write_text("\n".join(parts), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
