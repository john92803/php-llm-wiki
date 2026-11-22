---
title: 變數基礎（$、大小寫、傳值與引用）
slug: variables
sources: [S3.1, S5.1]
related: [[variable-scope]], [[variable-variables]], [[null]], [[constants]]
---
## 一句話說明
PHP 變數用 `$` 加變數名稱表示，名稱區分大小寫，指派預設是複製值 [S3.1]。

## 說明
有效的變數名稱以字母（`A-Z`、`a-z` 或 128 到 255 的位元組）或底線開頭，後面接任意數量的字母、數字或底線 [S3.1]。`$4site` 這種以數字開頭的名稱是非法的 [S3.1]。

`$this` 是特殊變數，不能被賦值 [S3.1]。

變數預設是傳值指派：把一個變數的值指派給另一個變數後，改變其中一個不會影響另一個 [S3.1]。

引用指派：在來源變數前加 `&`（`$bar = &$foo`），新變數就成為原變數的別名，改動任一個都會影響另一個 [S3.1]。只有有名字的變數才能被引用指派 [S3.1]。

PHP 不需要宣告變數，但宣告是很好的做法 [S3.1]。存取未定義的變數會產生 `E_WARNING`（PHP 8.0.0 之前是 `E_NOTICE`），預設值是 `null`；可以用 `isset()` 檢查變數是否已初始化 [S3.1]。對未定義的變數附加元素（`$arr[] = 'value'`）會自動建立新陣列，不會產生警告 [S3.1]。用 `unset()` 銷毀變數 [S3.1]。

指派本身也是一個表達式，值是被指派的值，所以可以寫 `$b = $a = 5` [S5.1]。

## 範例
```php
<?php
$var = 'Bob';
$Var = 'Joe';
echo "$var, $Var", PHP_EOL;      // 名稱區分大小寫

$foo = 'Bob';
$bar = $foo;                     // 傳值
$bar = 'Alice';
echo $foo, PHP_EOL;

$ref = &$foo;                    // 引用
$ref = "My name is $ref";
echo $foo, PHP_EOL;
?>
```
輸出（PHP 8.3.6 實測）：
```text
Bob, Joe
Bob
My name is Bob
```

## 常見陷阱
- `$var` 和 `$Var` 是兩個不同的變數 [S3.1]
- 打錯變數名稱不會報錯中斷，只會有警告並得到 `null` [S3.1]
- 被 include 的檔案用了同名變數時，依賴未初始化變數的預設值會出問題 [S3.1]

## 出處
- [S3.1] https://www.php.net/manual/zh/language.variables.basics.php
- [S5.1] https://www.php.net/manual/zh/language.expressions.php
