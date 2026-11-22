---
title: 型別轉換（Type Juggling）
slug: type-juggling
sources: [S2.1, S2.4, S2.5, S2.6, S2.7, S2.9]
related: [[type-system]], [[truthy-falsy]], [[integer]], [[float]], [[strings]], [[expressions]]
---
## 一句話說明
PHP 會依照「上下文」自動把值轉成需要的型別，也可以用 `(int)`、`(string)` 等語法強制轉型 [S2.9]。

## 說明
PHP 可能會在某些上下文中自動把值轉換為另一種型別；上下文有：數字、字串、邏輯、整數和字串、比較、函式 [S2.9]。值被解釋為不同型別時，值本身的型別不會改變 [S2.9]。

數字上下文（算術運算子）：任一運算元是 float（或不能解釋為 int）時，兩者都解釋為 float、結果是 float；否則結果是 int [S2.9]。自 PHP 8.0.0 起，無法解釋的運算元會丟出 TypeError [S2.9]。

字串上下文（echo、print、字串插值、字串連接運算子）：值會被解釋為 string [S2.9]。

邏輯上下文（條件語句、三元運算子、邏輯運算子）：值會被解釋為 bool，規則見 [[truthy-falsy]] [S2.9][S2.4]。

整數和字串上下文（位元運算子）：所有運算元都是 string 時結果是 string，否則解釋為 int [S2.9]。

比較上下文的轉換規則在手冊的「型別比較表」中說明 [S2.9]。

函式上下文：把值傳給有宣告型別的參數、屬性，或從有宣告回傳型別的函式回傳時，值必須符合型別；例外是 int 可以轉成 float，以及在強制型別模式（預設）下純量值可以被轉換 [S2.9]。內部函式自動把 `null` 轉成純量型別，自 PHP 8.1.0 起棄用 [S2.9]。

強制轉型：在值前面的括號中寫型別，允許的有 `(int)`、`(bool)`、`(float)`、`(string)`、`(array)`、`(object)`、`(unset)` [S2.9]。括號中的空格會被忽略 [S2.9]。`(integer)`、`(boolean)`、`(binary)`、`(double)` 這些不標準的別名自 PHP 8.5.0 起棄用 [S2.9]。`(unset)` 自 PHP 7.2.0 起棄用、PHP 8.0.0 起移除 [S2.9]。要直接改變變數本身的型別，用 `settype()` [S2.9][S2.1]。

string 轉數字：string 是數字或以數字開頭時，解析成對應的 int 或 float，否則是 `0` [S2.5][S2.6]。

## 範例
```php
<?php
$foo = 10;            // $foo 是 int
$str = "$foo";        // $str 是 string
$fst = (string) $foo; // $fst 也是 string

// 印出 "they are the same"
if ($fst === $str) {
    echo "they are the same", PHP_EOL;
}

var_dump("5" + 3);     // 數字上下文
var_dump(5 + 1.5);     // 有 float，結果是 float
var_dump(5 . 3);       // 字串上下文
var_dump((bool) $foo); // 強制轉型
?>
```
輸出（PHP 8.3.6 實測）：
```text
they are the same
int(8)
float(6.5)
string(2) "53"
bool(true)
```

## 常見陷阱
- 轉型只影響這次的運算結果，變數本身的型別不變 [S2.9]
- 字串 `"5"` 遇到 `+` 會被當數字，遇到 `.` 數字也會被當字串 [S2.9][S2.7]
- 不要再用 `(unset)`、`(real)`，已經移除 [S2.9]

## 出處
- [S2.1] https://www.php.net/manual/zh/language.types.intro.php
- [S2.4] https://www.php.net/manual/zh/language.types.boolean.php
- [S2.5] https://www.php.net/manual/zh/language.types.integer.php
- [S2.6] https://www.php.net/manual/zh/language.types.float.php
- [S2.7] https://www.php.net/manual/zh/language.types.string.php
- [S2.9] https://www.php.net/manual/zh/language.types.type-juggling.php
