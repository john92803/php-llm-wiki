#!/usr/bin/env python3
"""檢查節點：Wiki lint（CLAUDE.md §6.3）與簡報檢查（§6.4 第 5 步）。

用法：
  python3 tools/check.py wiki     # lint wiki/
  python3 tools/check.py slides   # 檢查 slides/index.html
  python3 tools/check.py all

每一項檢查都對應 CLAUDE.md 的一條規則；有任何 ERROR 時 exit code = 1，
代表流程要回到「生成」節點重做（只重做出錯的頁面／投影片）。
"""
import html
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
WIKI = ROOT / "wiki"
CONCEPTS = WIKI / "concepts"
SOURCES = WIKI / "sources"
SLIDES = ROOT / "slides" / "index.html"

ID_RE = re.compile(r"\[(S\d\.\d)\]")
LINK_RE = re.compile(r"\[\[([a-z0-9-]+)\]\]")
VER_RE = re.compile(r"PHP (\d+\.\d+(?:\.\d+)?)")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


# ---------- raw ----------
def load_raw() -> dict[str, dict]:
    """回傳 {S2.4: {"text": 原文, "fidelity": verbatim|summary}}"""
    out = {}
    for f in sorted(RAW.glob("*.md")):
        parts = re.split(r"^## \[(S\d\.\d)\][^\n]*\n", f.read_text(encoding="utf-8"), flags=re.M)
        for i in range(1, len(parts), 2):
            body = parts[i + 1]
            m = re.search(r"^- fidelity: (\w+)", body, flags=re.M)
            out[parts[i]] = {"text": body, "fidelity": m.group(1) if m else "unknown"}
    return out


# ---------- PHP 執行 ----------
PHP = ["php", "-n", "-d", "error_reporting=E_ALL", "-d", "display_errors=stdout",
       "-d", "html_errors=0"]


def php_lint(code: str, where: str) -> bool:
    with tempfile.NamedTemporaryFile("w", suffix=".php", delete=False) as t:
        t.write(code)
    r = subprocess.run(["php", "-l", t.name], capture_output=True, text=True)
    pathlib.Path(t.name).unlink()
    if r.returncode != 0:
        err(f"{where}: php -l 失敗：{(r.stdout + r.stderr).strip().splitlines()[0]}")
        return False
    return True


def php_run(code: str) -> str:
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "example.php"
        p.write_text(code, encoding="utf-8")
        r = subprocess.run(PHP + [str(p)], capture_output=True, text=True, cwd=d, timeout=10)
        return (r.stdout + r.stderr).replace(str(p), "example.php")


def norm(s: str) -> str:
    return "\n".join(line.rstrip() for line in s.strip("\n").splitlines()).strip()


def check_example(code: str, expected: str | None, where: str, mode: str = "run") -> None:
    if not php_lint(code, where):
        return
    if mode == "lint" or expected is None:
        return
    got = php_run(code)
    if norm(got) != norm(expected):
        err(f"{where}: 輸出不符\n    預期：{norm(expected)!r}\n    實際：{norm(got)!r}")


# ---------- wiki ----------
def frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def knowledge_lines(body: str, skip_sections=("出處", "相關概念", "範例")):
    """產生 (行號, 行) — 需要附出處的知識句。跳過程式碼、標題、出處等段落。"""
    in_code = False
    section = ""
    for n, line in enumerate(body.splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.startswith("#"):
            section = line.lstrip("#").strip()
            continue
        s = line.strip()
        if not s or s.startswith(">") and len(s) < 3:
            continue
        if any(section.startswith(x) for x in skip_sections):
            continue
        if s in ("輸出：",) or s.startswith("輸出（"):
            continue
        yield n, s, section


def lint_wiki(raw: dict) -> None:
    pages = {p.stem: p for p in CONCEPTS.glob("*.md")}
    srcpages = list(SOURCES.glob("*.md"))
    inbound = {slug: 0 for slug in pages}
    missing_links: dict[str, set] = {}
    index_text = (WIKI / "index.md").read_text(encoding="utf-8")

    for p in list(pages.values()) + srcpages:
        rel = p.relative_to(ROOT)
        text = p.read_text(encoding="utf-8")
        meta, body = frontmatter(text)
        offset = text[: len(text) - len(body)].count("\n")
        if not meta:
            err(f"{rel}: 缺少 frontmatter")
        declared = set(re.findall(r"S\d\.\d", meta.get("sources", meta.get("subpages", ""))))

        # 1. 每句知識都要有出處，而且出處在 raw/ 找得到
        for n, line, section in knowledge_lines(body):
            n += offset
            ids = ID_RE.findall(line)
            if not ids:
                err(f"{rel}:{n}: 缺出處 ID → {line[:50]}")
                continue
            for i in ids:
                if i not in raw:
                    err(f"{rel}:{n}: 出處 [{i}] 不在 raw/")
                elif declared and i not in declared:
                    err(f"{rel}:{n}: 出處 [{i}] 沒列在 frontmatter sources")
                # 2. summary 等級的出處要標註
                elif raw[i]["fidelity"] == "summary" and "（summary）" not in line:
                    err(f"{rel}:{n}: [{i}] 只有 summary 等級，需標註（summary）")
            # 7. 版本號必須出現在所引用的原文
            for v in VER_RE.findall(line):
                if not any(v in raw.get(i, {}).get("text", "") for i in ids):
                    err(f"{rel}:{n}: 版本 PHP {v} 在引用的 {ids} 原文中找不到")

        # 3/4. 連結
        for slug in set(LINK_RE.findall(text)):
            if slug in pages:
                if p.stem != slug:
                    inbound[slug] += 1
            else:
                missing_links.setdefault(slug, set()).add(str(rel))

        # 6. 範例：```php 區塊；後面接「輸出：」+ ```text 就要比對
        blocks = list(re.finditer(r"```php\n(.*?)```(\s*\n輸出[^\n]*\n```text\n(.*?)```)?", body, flags=re.S))
        for k, m in enumerate(blocks, 1):
            code = m.group(1)
            if "<?php" not in code:
                continue  # 片段（例如語法示意），不執行
            check_example(code, m.group(3), f"{rel} 範例#{k}")

        # 8. index 列出所有頁面
        if str(p.relative_to(WIKI)) not in index_text:
            err(f"{rel}: 沒有列在 wiki/index.md")

    for slug, n in inbound.items():
        if n == 0:
            err(f"concepts/{slug}.md: 孤兒頁（沒有其他頁面連過來）")
    for slug, refs in sorted(missing_links.items()):
        warn(f"待建頁面 [[{slug}]]（被 {', '.join(sorted(refs))} 連結）")


# ---------- slides ----------
def lint_slides(raw: dict) -> None:
    from bs4 import BeautifulSoup
    import opencc

    if not SLIDES.exists():
        err("slides/index.html 不存在")
        return
    soup = BeautifulSoup(SLIDES.read_text(encoding="utf-8"), "html.parser")
    slides = soup.select("section.slide")
    if not 12 <= len(slides) <= 16:
        err(f"投影片 {len(slides)} 張，規格建議 12–16 張")
    for tag in soup.find_all(["script", "link"]):
        src = tag.get("src") or tag.get("href") or ""
        if src.startswith("http"):
            err(f"引用外部資源（不可依賴 CDN）：{src}")

    concept_sources = {}
    for p in CONCEPTS.glob("*.md"):
        meta, _ = frontmatter(p.read_text(encoding="utf-8"))
        concept_sources[p.stem] = set(re.findall(r"S\d\.\d", meta.get("sources", "")))

    s2t = opencc.OpenCC("s2t")
    for n, s in enumerate(slides, 1):
        where = f"slide {n}「{s.find(['h1', 'h2']).get_text(strip=True) if s.find(['h1', 'h2']) else '?'}」"
        concepts = [c for c in s.get("data-concepts", "").split(",") if c]
        foot = s.select_one(".src")
        ids = ID_RE.findall(foot.get_text()) if foot else []
        kind = s.get("data-kind", "content")
        if kind == "content":
            if not concepts:
                err(f"{where}: 沒有標 data-concepts（追不到概念頁）")
            if not ids:
                err(f"{where}: 頁尾沒有出處 ID")
        for c in concepts:
            if c not in concept_sources:
                err(f"{where}: 概念頁 {c} 不存在")
        allowed = set().union(*(concept_sources.get(c, set()) for c in concepts)) if concepts else set()
        for i in ids:
            if i not in raw:
                err(f"{where}: 出處 [{i}] 不在 raw/")
            elif concepts and i not in allowed:
                err(f"{where}: 出處 [{i}] 不在概念頁 {concepts} 的 sources 裡")

        # 程式碼：執行並比對輸出
        for k, pre in enumerate(s.select("pre.code"), 1):
            code = pre.get_text()
            out = pre.find_next_sibling("pre")
            expected = out.get_text() if out is not None and "output" in out.get("class", []) else None
            check_example(code, expected, f"{where} 程式碼#{k}", pre.get("data-check", "run"))

        # 簡體字
        text = s.get_text(" ")
        conv = s2t.convert(text)
        bad = sorted({a for a, b in zip(text, conv) if a != b})
        if bad:
            err(f"{where}: 疑似簡體字 {''.join(bad)}")


def main() -> int:
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    raw = load_raw()
    if what in ("wiki", "all"):
        lint_wiki(raw)
    if what in ("slides", "all"):
        lint_slides(raw)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
