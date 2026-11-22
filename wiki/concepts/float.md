---
title: 浮點數（float）
slug: float
sources: [S2.5, S2.6, S2.9]
related: [[integer]], [[type-juggling]]
---
## 一句話說明
float（也叫 double 或 real）的精度有限，永遠不要直接比較兩個浮點數是否相等 [S2.6]。

## 說明
float 可以寫成 `1.234`、`1.2e3`、`7E-10`，從 PHP 7.4.0 開始也可以用底線，例如 `1_234.567` [S2.6]。

float 的字長和平台有關，通常最大值是 1.8e308，具有 14 位十進位數字的精度（64 位元 IEEE 格式）[S2.6]。

PHP 通常使用 IEEE 754 雙精度格式，取整造成的最大相對誤差是 1.11e-16 [S2.6]。像 `0.1`、`0.7` 這種十進位能精確表示的數，在內部的二進位格式中無法精確表示 [S2.6]。所以 `floor((0.1+0.7)*10)` 通常會回傳 `7` 而不是 `8`，因為內部值類似 `7.9999999999999991118...` [S2.6]。

要比較浮點數，改用「差值小於一個很小的誤差值（epsilon）」的方式 [S2.6]。需要更高精度時，使用任意精度數學函式或 gmp 函式 [S2.6]。

`NAN` 代表未定義或無法表示的值；拿 `NAN` 和任何值（除了 `true`）做鬆散或嚴格比較，結果都是 `false`，要用 `is_nan()` 檢查 [S2.6]。

string 是數字或以數字開頭時，會解析成對應的 float，否則轉換為 `0` [S2.6]。算術運算中只要有一個運算元是 float，結果就是 float [S2.9]。

## 範例
```php
<?php
var_dump(floor((0.1+0.7)*10));

$a = 1.23456789;
$b = 1.23456780;
$epsilon = 0.00001;

if (abs($a - $b) < $epsilon) {
    echo "true";
}
?>
```
輸出（PHP 8.3.6 實測）：
```text
float(7)
true
```

## 常見陷阱
- `floor((0.1+0.7)*10)` 是 7 不是 8 [S2.6]
- 用 `==` 比較兩個 float 結果不可靠，要用 epsilon [S2.6]
- `NAN` 連跟自己比較都不相等，要用 `is_nan()` [S2.6]
- 超出 int 範圍的 float 轉 int 沒有警告、結果未定義 [S2.5]

## 出處
- [S2.5] https://www.php.net/manual/zh/language.types.integer.php
- [S2.6] https://www.php.net/manual/zh/language.types.float.php
- [S2.9] https://www.php.net/manual/zh/language.types.type-juggling.php
