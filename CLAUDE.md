# CLAUDE.md — PHP 語言基礎 LLM Wiki

這份檔案是這個 Wiki 的 schema，也就是 LLM 的操作手冊。每次開始工作前先讀完這份檔案、`wiki/index.md` 和 `wiki/log.md` 的最後 10 筆紀錄。

## 1. 目的與範圍

- **主題**：PHP 語言基礎（基本語法、型別、變數、常數、表達式）
- **用途**：當作知識庫，產生「PHP 基礎入門」教學 HTML 簡報
- **讀者**：寫過其他程式語言（例如 Python、C、JavaScript），但沒有碰過 PHP 的人。不用解釋「什麼是變數」，重點放在 **PHP 和其他語言不一樣的地方**。
- **語言**：Wiki 和簡報都用**繁體中文**。`raw/` 保留官方手冊原文（簡體中文）。技術名詞可以保留英文（例如 heredoc、type juggling）。

## 2. 目錄結構

```
php-llm-wiki/
├── CLAUDE.md            # 本檔：schema
├── raw/                 # 原始資料。不可修改（immutable）
│   ├── 01-basic-syntax.md
│   ├── 02-types.md
│   ├── 03-variables.md
│   ├── 04-constants.md
│   └── 05-expressions.md
├── wiki/
│   ├── index.md         # 所有頁面的目錄，每頁一行摘要
│   ├── log.md           # 依時間記錄每次操作
│   ├── sources/         # 每個 source 一頁摘要（S1–S5）
│   └── concepts/        # 概念頁，一個概念一頁
└── slides/
    ├── outline.md       # 簡報大綱（先給使用者確認）
    └── index.html       # 最後的教學簡報
```

## 3. 來源清單與 ID

每個 source 有一個 ID，子頁面用 `S<章>.<節>` 標示。Wiki 引用時一律用這組 ID。

| ID | 章節 | 子頁面 |
|---|---|---|
| S1 | 基本語法 `language.basic-syntax` | S1.1 PHP 標記、S1.2 從 HTML 中分離、S1.3 指令分隔符、S1.4 註解 |
| S2 | 類型 `language.types` | S2.1 簡介、S2.2 型別系統、S2.3 NULL、S2.4 Boolean、S2.5 Integer、S2.6 Float、S2.7 String、S2.8 Array、S2.9 型別轉換 |
| S3 | 變數 `language.variables` | S3.1 基礎、S3.2 作用域、S3.3 可變變數、S3.4 預定義變數 |
| S4 | 常數 `language.constants` | S4.1 語法、S4.2 魔術常數 |
| S5 | 表達式 `language.expressions` | S5.1 表達式（本頁就有正文） |

網址格式：`https://www.php.net/manual/zh/<頁面>.php`

## 4. 資料可信度規則（最重要）

這個 Wiki 第一次執行時發現：**5 個章節首頁都只有目錄**，WebFetch 會用模型自己的知識補內容，看起來很像文件、其實沒有出處。所以加上以下規則：

1. **只抓子頁面**，不要從章節目錄頁擷取知識。
2. 抓取時要求「逐字輸出正文、不要摘要、不要補充、忽略 User Contributed Notes」。
3. 每段原文在 `raw/` 裡要標 `fidelity`：
   - `verbatim`：逐字正文
   - `summary`：工具只給了摘要。可以用一個更窄的 prompt（只要求特定小節）**重試一次**，還是摘要就保留並標記。
4. 工具輸出裡出現「非來自頁面」「依一般知識」「用戶備註」這類字眼的內容，**一律丟掉**，不能寫進 `raw/`。
5. `raw/` 寫入後就不能修改。要補內容就新增一個段落，並在 log 記錄。
6. Wiki 裡的每一條知識都要附上出處 ID，例如 `[S2.4]`。找不到出處的句子不能寫。
7. 版本差異（例如「PHP 8.0.0 起」）必須照原文寫，不能自己推論。

## 5. 頁面格式

### 5.1 Source 頁（`wiki/sources/S1-basic-syntax.md`）

```markdown
---
id: S1
title: 基本語法
raw: raw/01-basic-syntax.md
subpages: [S1.1, S1.2, S1.3, S1.4]
fidelity: 4/4 verbatim
ingested: YYYY-MM-DD
---
## 摘要
（3–5 句，繁體中文）
## 重點
- 重點一 [S1.1]
## 跟其他語言不同的地方
- …… [S1.3]
## 相關概念
[[php-tags]]、[[comments]]
```

### 5.2 概念頁（`wiki/concepts/<slug>.md`）

```markdown
---
title: 型別轉換（Type Juggling）
slug: type-juggling
sources: [S2.9, S2.4, S2.5]
related: [[truthy-falsy]], [[strict-comparison]]
---
## 一句話說明
## 說明
（每段結尾附出處 ID）
## 範例
（從 raw 原文取，或自己寫但要實際執行驗證過）
## 常見陷阱
## 出處
- [S2.9] https://www.php.net/manual/zh/language.types.type-juggling.php
```

- 概念頁的 slug 用英文 kebab-case。
- 用 `[[slug]]` 互相連結。連到還不存在的頁面沒關係，lint 時會列出來。

## 6. 操作流程

### 6.1 Ingest（先討論、後生成）

一次只 ingest 一個 source：

1. **讀取**：讀 `raw/0X-*.md`，確認每個子頁面的 fidelity。
2. **討論**（不寫檔）：給使用者看：
   - 這個 source 的 3–5 個重點
   - 預計新增或更新哪些概念頁
   - 和已存在的頁面有沒有重複或矛盾
   - 哪些內容只有 summary 等級的來源
3. **等使用者確認或調整**。沒有確認就不能生成。
4. **生成**：寫 source 頁、新增或更新概念頁。
5. **更新** `index.md` 和 `log.md`，log 要記錄使用者在討論時做的決定。

### 6.2 Query

1. 先讀 `index.md` 找相關頁面，再讀頁面本身。
2. 只用 Wiki 的內容回答，並附上出處 ID。
3. Wiki 裡沒有的就回答「Wiki 中沒有這個資訊」，**不要用自己的知識補**。
4. 如果回答整合出新的見解，詢問使用者要不要存成概念頁。

### 6.3 Lint

依序檢查，能修的先修，其餘列出來回報：

- [ ] 每一句知識都有出處 ID，而且該 ID 在 `raw/` 裡找得到對應內容
- [ ] 出處只有 `summary` 等級的句子有標註
- [ ] 沒有孤兒頁（沒有任何頁面連過來）
- [ ] `[[連結]]` 指向的頁面都存在，不存在的列成待建清單
- [ ] 頁面之間沒有互相矛盾（特別是版本號、預設值）
- [ ] 程式範例能執行（`php -l` 語法檢查；有寫輸出的範例要實際跑過、比對輸出）
- [ ] `index.md` 列出所有頁面

### 6.4 產生簡報（slides）

```
查詢 Wiki → 產生大綱 → 使用者確認 → 逐張生成 → 檢查 → 輸出 HTML
                ↑            │                      │
                └── 修改 ────┘    不通過 ← ──────────┘
```

1. **查詢 Wiki**：從 `index.md` 選出要教的概念，依「從簡單到難」排序。
2. **產生大綱**：寫進 `slides/outline.md`，每張投影片列出：標題、要教的一個重點、使用的概念頁、出處 ID。
3. **使用者確認大綱**。不確認就不生成 HTML。
4. **逐張生成**：每張只講一個重點，搭配一個短範例。
5. **檢查**（每張都要過）：
   - 內容能追到 Wiki 的概念頁，再追到 `raw/`（不能出現 Wiki 沒有的知識）
   - 程式範例實際執行過，標示的輸出和執行結果一致
   - 用語是繁體中文，沒有混入簡體字
   - 每張頁尾標示出處 ID
6. 不通過的投影片**只重新生成那一張**，回到第 4 步；如果問題出在 Wiki 內容本身，先回去修概念頁（並記錄在 log），再重新生成。
7. 最後用瀏覽器實際打開 `slides/index.html`，確認版面、換頁、程式碼區塊都正常。

### 簡報規格

- 單一 HTML 檔，不依賴外部 CDN，打開就能用
- 用鍵盤左右鍵換頁，並顯示頁碼
- 建議 12–16 張：封面 → 學習目標 → 各主題 → 常見陷阱總整理 → 小測驗 → 出處
- 程式碼區塊用等寬字體，關鍵行要標示出來

## 7. log.md 格式

```markdown
## [YYYY-MM-DD HH:MM] ingest | S2 類型
- 討論：使用者決定 ……
- 新增：concepts/type-juggling.md、concepts/truthy-falsy.md
- 更新：concepts/strict-comparison.md
- 問題：S2.9 首次抓取只有摘要，改用窄 prompt 重抓後為 verbatim
```

操作類型：`fetch`、`ingest`、`query`、`lint`、`slides`、`fix`

## 8. 禁止事項

- 不要修改 `raw/`
- 不要在沒有討論、沒有確認的情況下生成 Wiki 頁或簡報
- 不要用模型自己的知識補 Wiki 沒有的內容
- 不要把 User Contributed Notes 當作官方內容
- 不要猜版本號；原文沒寫就不寫
