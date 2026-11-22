---
title: 可變變數（$$a）
slug: variable-variables
sources: [S3.1, S3.3, S3.4]
related: [[variables]], [[superglobals]], [[string-interpolation]]
---
## 一句話說明
可變變數拿一個變數的值當作另一個變數的名稱，寫法是兩個 `$`，例如 `$$a` [S3.3]。

## 說明
如果 `$a = 'hello'`，那麼 `$$a = 'world'` 會定義 `$hello`，內容是 `'world'` [S3.3]。

用在陣列時有歧義：`${$a[1]}` 表示把 `$a[1]` 的值當變數名稱，`${$a}[1]` 表示取 `$$a` 這個變數的索引 `[1]` [S3.3]。

物件屬性也可以用可變名稱存取，例如 `$foo->$bar`，也可以用大括號 `$foo->{$start . $end}` 劃清界線 [S3.3]。

不符合命名規則的變數名稱只能在執行時動態存取，例如 `${'invalid-name'}` [S3.1]。

在函式和類別方法中，超全域變數不能當作可變變數；`$this` 也不能被動態引用 [S3.3][S3.4]。

## 範例
```php
<?php
$a = 'hello';
$$a = 'world';
echo "$a {$$a}", PHP_EOL;
echo "$a $hello", PHP_EOL;
?>
```
輸出（PHP 8.3.6 實測）：
```text
hello world
hello world
```

## 常見陷阱
- `$$a[1]` 有歧義，要用 `${$a[1]}` 或 `${$a}[1]` 寫清楚 [S3.3]
- 在函式裡不能用 `$$name` 動態存取超全域變數 [S3.3]

## 出處
- [S3.1] https://www.php.net/manual/zh/language.variables.basics.php
- [S3.3] https://www.php.net/manual/zh/language.variables.variable.php
- [S3.4] https://www.php.net/manual/zh/language.variables.predefined.php
