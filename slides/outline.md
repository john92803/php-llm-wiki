# 簡報大綱：PHP 基礎入門（給寫過 Python／C／JavaScript 的人）

> 決定：使用者指示「不用討論，直接製作」，因此跳過 CLAUDE.md §6.4 第 3 步的使用者確認，大綱產生後直接逐張生成（已記錄在 wiki/log.md）。
> 排序：從簡單到難。16 張（規格 12–16）。每張只教一個重點、一個短範例，內容只取自 Wiki 概念頁。

| # | 標題 | 要教的一個重點 | 概念頁 | 出處 |
|---|---|---|---|---|
| 1 | 封面：PHP 基礎入門 | 主題與對象（封面，非內容頁） | — | — |
| 2 | 學習目標 | 本簡報要帶走的 5 件事（非內容頁） | — | — |
| 3 | PHP 標記 | 只有 `<?php ... ?>` 之間會被執行；`<?php` 後要空白；純 PHP 檔省略結尾 `?>` | php-tags | S1.1, S1.3 |
| 4 | `?>` 的副作用 | 標籤外原樣輸出；`?>` 隱含分號並吃掉後面一個換行；單行註解遇 `?>` 就結束 | html-embedding, statement-separation, comments | S1.2, S1.3, S1.4 |
| 5 | 動態型別 | 變數不宣告型別，型別跟著值走；用 `get_debug_type()`／`var_dump()` 檢查 | type-system | S2.1, S2.9 |
| 6 | 真假值 | 轉 bool 為 false 的值很少，但 `"0"` 是 false、`"false"` 是 true | truthy-falsy | S2.4 |
| 7 | 整數與浮點數 | `0123` 是八進位、溢位變 float、沒有整數除法運算子、float 精度 | integer, float | S2.5, S2.6 |
| 8 | 字串 | 單引號不插值、雙引號插值；連接用 `.` 不是 `+`；複雜運算式用 `{$...}` | strings, string-interpolation | S2.7, S2.8 |
| 9 | 陣列 | array 是有序映射；`unset()` 不重建索引；指派會複製 | arrays | S2.8 |
| 10 | 型別轉換與比較 | 依上下文自動轉換；`==` 與 `===` 的差別 | type-juggling, expressions | S2.9, S5.1 |
| 11 | 變數：傳值與引用 | `$` 開頭、區分大小寫；預設傳值，`&` 才是引用 | variables | S3.1 |
| 12 | 作用域 | 函式看不到全域變數（和 C 不同）；用 `global` | variable-scope, superglobals | S3.2, S3.4 |
| 13 | 常數 | `const`／`define()`、不加 `$`、未定義常數丟 Error；魔術常數 | constants, magic-constants | S4.1, S4.2 |
| 14 | 常見陷阱總整理 | 把前面 8 個「和其他語言不同」的陷阱放在一頁 | truthy-falsy, strings, integer, float, arrays, statement-separation, variable-scope, constants | S2.4, S2.7, S2.5, S2.6, S2.8, S1.3, S3.2, S4.1 |
| 15 | 小測驗 | 三題自我檢查（答案點開才顯示） | truthy-falsy, strings, variable-scope | S2.4, S2.7, S3.2 |
| 16 | 出處 | 列出 S1–S5 來源（非內容頁） | — | S1–S5 |

## 排除的內容
Wiki 沒有收錄的主題（類別、函式定義細節、迴圈語法、運算子優先順序等）不放進簡報。
