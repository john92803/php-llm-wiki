# Wiki 目錄

> 每頁一行摘要。新增頁面時同步更新。

## Sources

- [sources/S1-basic-syntax.md](sources/S1-basic-syntax.md) — S1 基本語法：PHP 標記、嵌入 HTML、分號、註解
- [sources/S2-types.md](sources/S2-types.md) — S2 類型：動態型別、null／bool／int／float／string／array、型別轉換
- [sources/S3-variables.md](sources/S3-variables.md) — S3 變數：`$`、傳值／引用、作用域、可變變數、超全域變數
- [sources/S4-constants.md](sources/S4-constants.md) — S4 常數：`const`／`define()`、魔術常數
- [sources/S5-expressions.md](sources/S5-expressions.md) — S5 表達式：指派的值、遞增、比較、三元

## Concepts

### 基本語法
- [concepts/php-tags.md](concepts/php-tags.md) — `<?php`、`<?=`、短標籤、省略結尾 `?>`
- [concepts/html-embedding.md](concepts/html-embedding.md) — 標籤外內容原樣輸出、條件區塊
- [concepts/statement-separation.md](concepts/statement-separation.md) — 分號、`?>` 隱含分號並吃掉換行
- [concepts/comments.md](concepts/comments.md) — `//`、`#`、`/* */`，單行註解遇 `?>` 結束

### 類型
- [concepts/type-system.md](concepts/type-system.md) — 動態型別、內建型別、`var_dump()`／`get_debug_type()`
- [concepts/null.md](concepts/null.md) — 唯一值 null、未定義變數、null 轉其他型別
- [concepts/truthy-falsy.md](concepts/truthy-falsy.md) — 哪些值轉 bool 是 false（`"0"`、空陣列…）
- [concepts/integer.md](concepts/integer.md) — 進位表示、溢位變 float、沒有整數除法運算子
- [concepts/float.md](concepts/float.md) — 精度問題、epsilon 比較、NAN
- [concepts/strings.md](concepts/strings.md) — 位元組字串、單／雙引號、`.` 連接、下標
- [concepts/heredoc-nowdoc.md](concepts/heredoc-nowdoc.md) — 多行字串、結束識別字縮排規則
- [concepts/string-interpolation.md](concepts/string-interpolation.md) — `$var`、`{$expr}` 插值
- [concepts/arrays.md](concepts/arrays.md) — 有序映射、key 強制轉換、`unset()` 不重建索引、複製語意
- [concepts/type-juggling.md](concepts/type-juggling.md) — 依上下文自動轉換、強制轉型

### 變數
- [concepts/variables.md](concepts/variables.md) — `$`、名稱區分大小寫、傳值 vs 引用、未定義變數
- [concepts/variable-scope.md](concepts/variable-scope.md) — 函式看不到全域變數、`global`、`$GLOBALS`、`static`
- [concepts/variable-variables.md](concepts/variable-variables.md) — `$$a`、`${$a[1]}`
- [concepts/superglobals.md](concepts/superglobals.md) — 每個作用域都可用的預定義陣列

### 常數
- [concepts/constants.md](concepts/constants.md) — `const` vs `define()`、不加 `$`、未定義常數丟 Error
- [concepts/magic-constants.md](concepts/magic-constants.md) — `__LINE__`、`__FILE__`、`__DIR__`、`__FUNCTION__`

### 表達式
- [concepts/expressions.md](concepts/expressions.md) — 指派是表達式、前／後遞增、`==` vs `===`、三元
