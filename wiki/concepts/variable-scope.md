---
title: 變數作用域（global、$GLOBALS、static）
slug: variable-scope
sources: [S3.2, S3.4]
related: [[variables]], [[superglobals]], [[constants]]
---
## 一句話說明
PHP 只有函式作用域和全域作用域，函式裡看不到外面的全域變數 [S3.2]。

## 說明
在函式之外定義的變數只屬於全域作用域；在命名函式或匿名函式裡建立的變數只屬於函式本體 [S3.2]。箭頭函式則會綁定父作用域的變數 [S3.2]。被 include 的檔案會繼承 include 那一行所在的作用域 [S3.2]。

這和 C 不同：C 的全域變數會自動提供給函式，PHP 的全域變數在函式中使用時必須宣告為 `global` [S3.2]。在函式裡直接使用全域變數，會被當成未定義的區域變數，產生 `E_WARNING`（PHP 8.0.0 之前是 `E_NOTICE`）[S3.2]。

`global $a, $b;` 會建立引用同名全域變數的區域變數 [S3.2]。也可以用超全域陣列 `$GLOBALS['a']` 存取全域變數，它的鍵名是變數名稱 [S3.2]。

`static` 變數只存在於函式作用域，但程式離開這個作用域時值不會遺失；它只在第一次呼叫時初始化 [S3.2]。PHP 8.3.0 之前，static 變數只能用常數表達式初始化；PHP 8.3.0 起也可以用函式呼叫等動態表達式 [S3.2]。

超全域變數（例如 `$_POST`）在每個作用域都自動可用，見 [[superglobals]] [S3.2][S3.4]。

## 範例
```php
<?php
$a = 1;
$b = 2;

function Sum()
{
    global $a, $b;

    $b = $a + $b;
}

Sum();
echo $b, PHP_EOL;

function counter()
{
    static $n = 0;
    $n++;
    return $n;
}
counter();
counter();
echo counter(), PHP_EOL;
?>
```
輸出（PHP 8.3.6 實測）：
```text
3
3
```

## 常見陷阱
- 在函式裡直接寫 `echo $a;` 讀不到外面的 `$a`，只會得到警告 [S3.2]
- 沒有 `static` 的區域變數每次呼叫都會重新初始化 [S3.2]
- `global` 是用引用實作的，在函式裡把 `global` 變數重新引用到別的變數，不會改到真正的全域變數 [S3.2]

## 出處
- [S3.2] https://www.php.net/manual/zh/language.variables.scope.php
- [S3.4] https://www.php.net/manual/zh/language.variables.predefined.php
