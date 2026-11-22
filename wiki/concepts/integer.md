---
title: 整數（int）
slug: integer
sources: [S2.5, S2.6, S2.9]
related: [[float]], [[type-juggling]], [[type-system]]
---
## 一句話說明
int 可以用十進位、十六進位、八進位、二進位表示；超出範圍會自動變成 float [S2.5]。

## 說明
八進位前面加 `0`，PHP 8.1.0 起也可以加 `0o` 或 `0O`；十六進位加 `0x`；二進位加 `0b` [S2.5]。從 PHP 7.4.0 開始，整數字面值可以包含底線 `_` 提升可讀性 [S2.5]。

int 的字長和平台有關：32 位元有號的最大值大約是二十億，64 位元平台通常大約是 9E18 [S2.5]。PHP 不支援無號 int [S2.5]。字長、最大值、最小值分別可以用常數 `PHP_INT_SIZE`、`PHP_INT_MAX`、`PHP_INT_MIN` 取得 [S2.5]。

整數溢位：數字超出 int 範圍會被解釋為 float；運算結果超出 int 範圍也會回傳 float [S2.5]。

PHP 沒有整數除法運算子，要用 `intdiv()`；`1/2` 會得到 float `0.5` [S2.5]。可以強制轉型為 int 捨去小數，或用 `round()` 四捨五入 [S2.5]。

float 轉 int 時向零取整 [S2.5]。自 PHP 8.1.0 起，非整數的 float 隱式轉成 int 而失去精度時，會發出棄用通知 [S2.5]。超出 int 範圍的 float 轉 int，結果是未定義的，而且沒有任何警告 [S2.5]。`NaN`、`Inf`、`-Inf` 轉成 int 是零 [S2.5]。

string 是數字或以數字開頭時，會被解析成對應的 int，否則轉換為 `0` [S2.5]。

算術運算時，如果任一運算元是 float，兩個運算元都會被解釋為 float，結果也是 float；否則結果是 int [S2.9]。

## 範例
```php
<?php
var_dump(0123);       // 八進位
var_dump(0x1A);       // 十六進位
var_dump(0b11111111); // 二進位
var_dump(1_234_567);  // PHP 7.4.0 起可用底線
var_dump(PHP_INT_MAX + 1);
var_dump(25/7);
var_dump((int) (25/7));
var_dump(round(25/7));
?>
```
輸出（PHP 8.3.6 實測，64 位元）：
```text
int(83)
int(26)
int(255)
int(1234567)
float(9.223372036854776E+18)
float(3.5714285714285716)
int(3)
float(4)
```

## 常見陷阱
- `0123` 不是 123，而是八進位的 83 [S2.5]
- `/` 永遠可能產生 float，`25/7` 不是 3 [S2.5]
- `round()` 回傳的是 float，不是 int [S2.5]
- 不要把未知的小數強制轉成 int：`(int) ((0.1+0.7) * 10)` 是 7 [S2.5]

## 出處
- [S2.5] https://www.php.net/manual/zh/language.types.integer.php
- [S2.6] https://www.php.net/manual/zh/language.types.float.php
- [S2.9] https://www.php.net/manual/zh/language.types.type-juggling.php
