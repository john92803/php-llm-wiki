---
title: 型別總覽（動態型別）
slug: type-system
sources: [S2.1, S2.2, S2.9, S5.1]
related: [[type-juggling]], [[null]], [[truthy-falsy]], [[integer]], [[float]], [[strings]], [[arrays]]
---
## 一句話說明
PHP 是動態型別語言：變數不用宣告型別，型別在執行時由值決定 [S2.1]。

## 說明
PHP 中每個表達式都屬於這些內建型別之一：null、bool、int、float、string、array、object、callable、resource [S2.1]。

變數宣告時不需要定義型別，型別由存放的值決定：把 string 指派給 `$var`，`$var` 就是 string；之後指派 int，它就變成 int [S2.9]。可以用型別宣告讓語言的某些部分靜態化 [S2.1]。

int、float、string、bool 是純量（scalar）型別 [S2.2][S5.1]；array 和 object 是複合型別 [S5.1]。

要檢查表達式的值和型別用 `var_dump()`；要取得型別用 `get_debug_type()`；要檢查是否屬於某型別則用 `is_` 開頭的函式（例如 `is_int()`）[S2.1]。PHP 8.0.0 之前沒有 `get_debug_type()`，可以改用 `gettype()`，但它不使用標準的型別名稱 [S2.1]。

型別可以組合：聯合型別寫成 `T|U|V`，交集型別寫成 `T&U&V` [S2.2]。PHP 內建兩個型別別名：`mixed` 和 `iterable`，不支援使用者自訂型別別名 [S2.2]。

型別限制了可以做的操作；如果值不支援某個操作，PHP 會嘗試把它轉換成支援的型別，詳見 [[type-juggling]] [S2.1]。

## 範例
```php
<?php
$a_bool = true;   // a bool
$a_str  = "foo";  // a string
$a_str2 = 'foo';  // a string
$an_int = 12;     // an int
echo get_debug_type($a_bool), "\n";
echo get_debug_type($a_str), "\n";

// 如果是整數，就加上 4
if (is_int($an_int)) {
    $an_int += 4;
}
var_dump($an_int);

// 如果 $a_bool 是字串，就印出來
if (is_string($a_bool)) {
    echo "String: $a_bool";
}
?>
```
輸出：
```text
bool
string
int(16)
```

## 常見陷阱
- 同一個變數可以先放 string 再放 int，型別會跟著改變，不會報錯 [S2.9]
- 在 PHP 8.0.0 之前的版本呼叫 `get_debug_type()` 無效 [S2.1]

## 出處
- [S2.1] https://www.php.net/manual/zh/language.types.intro.php
- [S2.2] https://www.php.net/manual/zh/language.types.type-system.php
- [S2.9] https://www.php.net/manual/zh/language.types.type-juggling.php
- [S5.1] https://www.php.net/manual/zh/language.expressions.php
