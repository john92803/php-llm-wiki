---
title: NULL
slug: null
sources: [S2.3, S2.4, S2.5, S2.7, S2.8, S3.1]
related: [[type-system]], [[variables]], [[truthy-falsy]]
---
## 一句話說明
null 型別只有一個值：不區分大小寫的常數 `null` [S2.3]。

## 說明
未定義的變數和被 `unset()` 的變數都會解析為 `null` [S2.3]。

存取未定義的變數會產生 `E_WARNING`（PHP 8.0.0 之前是 `E_NOTICE`），未定義變數的預設值是 `null` [S3.1]。可以用 `isset()` 檢查變數是否已初始化 [S3.1]。

null 轉成其他型別時：轉 bool 是 false [S2.4]，轉 int 是 `0` [S2.5]，轉 string 是空字串 [S2.7]，轉 array 是空陣列 [S2.8]；當陣列鍵時會變成 `""` [S2.8]。

`(unset) $var` 轉型自 PHP 7.2.0 起廢棄，PHP 8.0.0 起移除 [S2.3]。

## 範例
```php
<?php
var_dump($unset_var);
?>
```
輸出：
```text
Warning: Undefined variable $unset_var in example.php on line 2
NULL
```

## 常見陷阱
- 讀取沒定義的變數不會中斷程式，只會發出警告並得到 `null` [S3.1]
- `null` 當陣列鍵會變成空字串 `""`，可能覆蓋鍵為 `""` 的元素 [S2.8]

## 出處
- [S2.3] https://www.php.net/manual/zh/language.types.null.php
- [S2.4] https://www.php.net/manual/zh/language.types.boolean.php
- [S2.5] https://www.php.net/manual/zh/language.types.integer.php
- [S2.7] https://www.php.net/manual/zh/language.types.string.php
- [S2.8] https://www.php.net/manual/zh/language.types.array.php
- [S3.1] https://www.php.net/manual/zh/language.variables.basics.php
