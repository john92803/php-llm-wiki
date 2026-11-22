---
title: 常數（const 與 define）
slug: constants
sources: [S4.1, S2.8]
related: [[magic-constants]], [[variables]], [[variable-scope]], [[arrays]]
---
## 一句話說明
常數用 `const` 或 `define()` 定義，使用時不加 `$`，一旦定義就不能改變或取消 [S4.1]。

## 說明
定義常數有兩種方法：`const` 關鍵字和 `define()` 函式 [S4.1]。`define()` 允許把常數定義為一個表達式，`const` 有一些限制 [S4.1]。

`const` 必須在最頂端的作用域使用，因為它是在編譯時定義的；所以不能在函式內、迴圈內、`if` 或 `try`/`catch` 中用 `const` 定義常數 [S4.1]。

用 `const` 定義時只能包含純量資料（bool、int、float、string），也可以是表達式或 array [S4.1]。

取用常數只要寫名字，跟變數不同，不應該加 `$` [S4.1]。常數名稱是動態的時候可以用 `constant()` 取值，用 `defined()` 檢查是否定義 [S4.1]。

常數和變數的差異：常數沒有 `$`；常數可以不管變數作用域在任何地方定義和存取；常數定義後不能重新定義或取消定義；常數只能是純量值或陣列 [S4.1]。

使用未定義的常數會丟出 Error [S4.1]。PHP 8.0.0 之前，未定義的常數會被解釋成同名字串 [S4.1]。這也是為什麼陣列的字串鍵要加引號：`$foo[bar]` 的 `bar` 會被當成常數 [S2.8][S4.1]。

## 範例
```php
<?php
const GREETING = 'Hello World';
define('ANIMALS', array('dog', 'cat', 'bird'));

function show()
{
    echo GREETING, " / ", ANIMALS[1], PHP_EOL;  // 函式裡也能直接用
}
show();

try {
    echo Greeting;
} catch (Error $e) {
    echo get_class($e), ': ', $e->getMessage(), PHP_EOL;
}
?>
```
輸出（PHP 8.3.6 實測）：
```text
Hello World / cat
Error: Undefined constant "Greeting"
```

## 常見陷阱
- 在函式或 `if` 裡寫 `const` 不行，要改用 `define()` [S4.1]
- 常數名稱打錯大小寫（`Greeting` 和 `GREETING`）會變成未定義常數而丟出 Error [S4.1]
- 不要在常數前面加 `$` [S4.1]

## 出處
- [S2.8] https://www.php.net/manual/zh/language.types.array.php
- [S4.1] https://www.php.net/manual/zh/language.constants.syntax.php
