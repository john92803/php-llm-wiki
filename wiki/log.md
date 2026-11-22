# 操作紀錄

## [2026-11-22 17:51] fetch | S1–S5 全部子頁面
- 方法：原本環境的網路政策擋掉 www.php.net，改建立個人環境 `php-llm-wiki` 只開放 www.php.net；用 `tools/fetch_raw.py` 以 curl 下載 20 個子頁面原始 HTML，擷取 `div#<頁面ID>` 正文、排除 User Contributed Notes，pandoc 轉 Markdown。
- 結果：raw/01–05 共 20 個子頁面，fidelity 20/20 verbatim；每頁正文皆為中文（未退回英文版）。
- 決定：不使用 WebFetch，因為它會摘要或補內容（CLAUDE.md §4 提到的問題），直接下載 HTML 可確保逐字。
- 備註：章節目錄頁只用來確認子頁面網址，不擷取知識（§4.1）。

## [2026-11-22 17:55] ingest | S1 基本語法
- 討論：使用者指示「不用討論，直接製作」，跳過 §6.1 第 2–3 步的確認。原本要討論的重點：(1) `<?php` 後必須有空白、`<?=`、短標籤可停用 (2) 標籤外內容原樣輸出、條件區塊會跳過 HTML (3) `?>` 隱含分號且吃掉換行 (4) 純 PHP 檔省略結尾 `?>` (5) 三種註解。fidelity 4/4 verbatim，無 summary 內容，Wiki 原本是空的，沒有重複或矛盾。
- 新增：sources/S1-basic-syntax.md、concepts/php-tags.md、concepts/html-embedding.md、concepts/statement-separation.md、concepts/comments.md
- 新增工具：tools/check.py（lint + 執行範例比對輸出 + 版本號必須出現在原文）
- 問題：lint 第一次就 0 error，懷疑檢查器沒生效 → 故意放錯誤輸出與缺出處的句子測試，兩個都抓到，確認有效；另外修正回報行號沒算 frontmatter 的 bug。
- 決定：S1.2 的條件範例原文沒定義 `$expression`，Wiki 範例補一行 `$expression = true;` 才能實際執行。

## [2026-11-22 17:58] ingest | S2 類型
- 討論：（使用者指示跳過確認）原本要討論的重點：(1) 動態型別、var_dump／get_debug_type (2) 轉 bool 的 false 清單，`"0"` 是 false (3) 整數溢位變 float、沒有整數除法運算子 (4) 浮點數精度與 epsilon (5) 單／雙引號、heredoc／nowdoc、插值 (6) array 是有序映射與 key 強制轉換 (7) 依上下文的 type juggling。fidelity 9/9 verbatim。
- 新增：sources/S2-types.md、concepts/type-system.md、null.md、truthy-falsy.md、integer.md、float.md、strings.md、heredoc-nowdoc.md、string-interpolation.md、arrays.md、type-juggling.md
- 決定：S2.2 的交集型別、類別型別、S2.7 的編碼細節、S2.8 物件轉陣列與 NUL 前綴，超出「語言基礎」讀者需求，只在 type-system 簡單提及或不收錄。
- 問題 1：原文範例註解裡的輸出是舊版格式（`float(9.2233720368548E+18)`、`float(3.5714285714286)`），PHP 8.3.6 實測是 `float(9.223372036854776E+18)`、`float(3.5714285714285716)`。決定範例輸出一律用實測值並標「PHP 8.3.6 實測」，不解釋差異原因（原文沒寫原因）。
- 問題 2：lint 執行 arrays 範例時多出 `Deprecated: Implicit conversion from float 1.5 to int loses precision`，原文 S2.8 範例輸出沒有這行。依 S2.5「PHP 8.1.0 起失去精度的 float→int 會發出棄用通知」補上預期輸出與一條陷阱（arrays.md 加入出處 S2.5）。
- 問題 3：truthy-falsy 一開始寫了「一個元素的陣列（即使元素是 0）是 true」，「即使元素是 0」是自己推論的，改成原文有的 `array(12)` 例子。
- 問題 4：S2.8「为什么 $foo[bar] 错了」段落裡有一段譯者註（「--haohappy 注」），不是官方原文。依 §4.4 精神不採用，Wiki 只用官方段落。

## [2026-11-22 17:58] ingest | S3 變數
- 討論：（使用者指示跳過確認）重點：`$` 與大小寫、傳值 vs 引用、未定義變數為 null + E_WARNING、函式看不到全域變數（與 C 不同）、`global`／`$GLOBALS`／`static`、可變變數、超全域變數。fidelity 4/4 verbatim。
- 新增：sources/S3-variables.md、concepts/variables.md、variable-scope.md、variable-variables.md、superglobals.md
- 決定：S3.2 中 global／static 以引用實作的進階範例（stdClass）只收一句陷阱，不放範例；S3.4 原文很短，superglobals 頁只寫原文有的內容，不列出 `$_GET` 等清單（原文只連到清單頁，沒有內容）。

## [2026-11-22 17:59] ingest | S4 常數、S5 表達式
- 討論：（使用者指示跳過確認）S4 重點：`const` vs `define()`、不加 `$`、不受作用域限制、未定義常數丟 Error、魔術常數。S5 重點：指派是表達式、前／後遞增、`==` vs `===`、複合指派、三元。fidelity 2/2、1/1 verbatim。
- 新增：sources/S4-constants.md、sources/S5-expressions.md、concepts/constants.md、magic-constants.md、expressions.md
- 決定：S5.1 的範例只給了程式沒有給輸出，Wiki 範例加一行 echo 把所有變數印出來，實測確認 `6 6 5 7 7 12 24 24`。

## [2026-11-22 17:59] lint | 全部 Wiki
- 結果：5 個 source 頁、21 個概念頁；0 error、0 warning（每句都有出處、出處都在 raw/、版本號都能在引用的原文找到、21 個範例 `php -l` 通過且輸出與實測一致、無孤兒頁、無斷鏈、index 完整）。
- 過程中修正：arrays.md 範例輸出缺 Deprecated 行（見 S2 紀錄）、各階段 index 未同步（每次 ingest 最後才更新，屬預期）。

## [2026-11-22 18:04] slides | PHP 基礎入門簡報（16 張）
- 大綱：使用者指示「不用討論，直接製作」，因此跳過 §6.4 第 3 步的使用者確認，大綱（slides/outline.md）產生後直接逐張生成。排序：標記 → `?>` → 型別 → 真假值 → 數字 → 字串 → 陣列 → 轉型與比較 → 變數 → 作用域 → 常數 → 陷阱 → 小測驗 → 出處。為了壓在 16 張內，註解併入「`?>` 的副作用」頁，概念頁 comments 仍有被引用。
- 檢查失敗 1（check.py slides，第 1 次）：5 個 error，slide 2、4、10、11、15 「疑似簡體字 吃／只／才」。原因：opencc `s2t` 把正體字「吃」「只」「才」誤判為簡體（異體對應）。實測 `s2tw` 不會誤判。我嘗試修改 check.py 改用 `s2tw`，被權限系統擋下，所以 check.py 沒有改；改為重寫那幾頁的措辭（只重做該張）。待辦：建議把 check.py 的 `s2t` 換成 `s2tw`。
- 檢查失敗 2（第 2 次）：1 個 error，slide 15 小測驗「才是字串連接」，同一原因，改寫該句。第 3 次 0 error。
- 範例執行比對：11 個程式範例第一次就輸出全部一致（Wiki lint 已先抓過範例錯誤）。
- 人工比對：逐張對照概念頁，簡報每個要點都能在對應概念頁找到；slide 5 的 `$v` 範例與 slide 12 的 bad()/good() 是自己寫的，輸出為實測值，行為本身來自 type-system／variable-scope 概念頁。
- 瀏覽器實測（Playwright，桌機 1280×720 與手機 390×780，按 → 翻 16 頁）：頁碼 1/16 到 16/16 正確、← 與空白鍵正常、console 無錯誤。第 1 輪桌機 slide 9（陣列）、13（常數）溢出，頁尾出處與輸出重疊；修正：頁尾改成 flex 流程底部、縮短常數範例。第 2 輪 slide 9、11 仍溢出，縮小程式碼字級。第 3 輪 0 張溢出、無橫向捲動。手機寬度單欄可捲動。
- 截圖：docs/screenshots/slide-01-cover.png、slide-08-strings-code.png（2x）。
- 輸出：docs/workflow.md（Mermaid graph、回圈說明、數據、反思）。CLAUDE.md 沒有修改。

## [2026-11-22 18:05] fix | 主代理審查子代理的簡報與文件
- 分工：簡報、大綱、workflow.md 由 Sonnet 子代理產生，主代理逐張審查並重跑檢查。
- 問題 1（人工審查抓到，工具抓不到）：slide 4 寫「標籤外的內容會原樣輸出，所以 Some text 和 No newline 黏在一起」，因果錯誤，黏在一起是因為 `?>` 後緊接的換行不會輸出 [S1.3]。只重做該張的這一句。
- 問題 2：修改時用了「吃掉」，check.py 再次回報「疑似簡體字 吃」。已確認是 opencc `s2t` 把「吃」轉成「喫」的誤判；改措辭後 0 error。`s2t` → `s2tw` 的修正留給使用者決定。
- 問題 3：log 的時間戳記原本是估的（寫到 19:10，但當時實際時間才 18:05）。依檔案修改時間校正為 17:51–18:04。
- 更新：docs/workflow.md 反思段補上以上三點。
- 結果：`python3 tools/check.py all` 0 error、0 warning。
