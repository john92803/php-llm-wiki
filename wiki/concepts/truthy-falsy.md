---
title: 真假值（轉換為 bool）
slug: truthy-falsy
sources: [S2.4, S2.5, S2.7, S2.9, S5.1]
related: [[type-juggling]], [[null]], [[expressions]]
---
## 一句話說明
任何值放進 `if`、三元運算子或邏輯運算子時都會被解釋成 bool，只有少數幾個值是 false [S2.4][S2.9]。

## 說明
bool 只有兩個值 `true` 和 `false`，兩者都不區分大小寫 [S2.4]。

在條件語句、三元運算子或邏輯運算子的上下文中，值會被解釋為 bool [S2.9]；表達式在必要時會自動轉換為 bool [S5.1]。所以 `if ($x == TRUE)` 是不必要的，直接寫 `if ($x)` 即可 [S2.4]。

轉換為 bool 時，下列值是 `false`：`false` 本身、整數 `0`、浮點數 `0.0` 和 `-0.0`、空字串 `""` 和字串 `"0"`、沒有元素的陣列、null（包括尚未賦值的變數）[S2.4]。

其他所有值都是 `true`，包括 resource 和 `NAN` [S2.4]。`-1` 和其他非零值（不論正負）一樣都是 `true` [S2.4]。

要明確轉換可以用 `(bool)` [S2.4]。反方向：`true` 轉 string 是 `"1"`、`false` 轉 string 是 `""` [S2.7]；`true` 轉 int 是 `1`、`false` 轉 int 是 `0` [S2.5]。

## 範例
```php
<?php
var_dump((bool) "");        // bool(false)
var_dump((bool) "0");       // bool(false)
var_dump((bool) 1);         // bool(true)
var_dump((bool) -2);        // bool(true)
var_dump((bool) "foo");     // bool(true)
var_dump((bool) 2.3e5);     // bool(true)
var_dump((bool) array(12)); // bool(true)
var_dump((bool) array());   // bool(false)
var_dump((bool) "false");   // bool(true)
?>
```
輸出：
```text
bool(false)
bool(false)
bool(true)
bool(true)
bool(true)
bool(true)
bool(true)
bool(false)
bool(true)
```

## 常見陷阱
- 字串 `"0"` 是 false，但字串 `"false"` 是 true [S2.4]
- `-1` 是 true [S2.4]
- 空陣列是 false，但有任何元素的陣列（例如 `array(12)`）就是 true [S2.4]
- `echo false;` 什麼都不會印，因為 false 轉成 string 是空字串 [S2.7]

## 出處
- [S2.4] https://www.php.net/manual/zh/language.types.boolean.php
- [S2.5] https://www.php.net/manual/zh/language.types.integer.php
- [S2.7] https://www.php.net/manual/zh/language.types.string.php
- [S2.9] https://www.php.net/manual/zh/language.types.type-juggling.php
- [S5.1] https://www.php.net/manual/zh/language.expressions.php
