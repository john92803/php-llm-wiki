---
title: 預定義變數與超全域變數
slug: superglobals
sources: [S3.2, S3.4]
related: [[variable-scope]], [[variable-variables]]
---
## 一句話說明
PHP 提供一組預定義陣列，存放 web 伺服器、執行環境和使用者輸入的資料，在每個作用域都自動可用，稱為超全域變數（superglobals）[S3.4]。

## 說明
這些陣列在每個作用域內自動可用，所以也叫自動全域變數（autoglobals）或超全域變數 [S3.4]。PHP 沒有讓使用者自訂超全域變數的機制 [S3.4]。

例如在函式裡可以直接使用 `$_POST['name']`，不需要宣告 `global` [S3.2]。`$GLOBALS` 本身也是超全域變數，所以在任何地方都能用它存取全域變數 [S3.2]。

超全域變數不能在函式或類別方法中當作可變變數使用 [S3.4]。如果 `variables_order` 中某些變數沒有設定，對應的預定義陣列就是空的 [S3.4]。

## 範例
```php
<?php
$x = 'global x';

function show()
{
    echo $GLOBALS['x'], PHP_EOL;
}
show();
?>
```
輸出（PHP 8.3.6 實測）：
```text
global x
```

## 常見陷阱
- 一般的全域變數在函式內看不到，但超全域變數可以，不要搞混 [S3.2][S3.4]

## 出處
- [S3.2] https://www.php.net/manual/zh/language.variables.scope.php
- [S3.4] https://www.php.net/manual/zh/language.variables.predefined.php
