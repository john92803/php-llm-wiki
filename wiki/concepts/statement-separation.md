---
title: 指令分隔符（分號與結束標籤）
slug: statement-separation
sources: [S1.3, S5.1]
related: [[php-tags]], [[html-embedding]], [[expressions]]
---
## 一句話說明
PHP 跟 C、Perl 一樣用分號結束語句，但結束標籤 `?>` 隱含一個分號 [S1.3]。

## 說明
PHP 需要在每個語句後面用分號結束指令 [S1.3]。

一段 PHP 程式碼的結束標籤隱含一個分號，所以 PHP 程式碼段的最後一行可以不寫分號 [S1.3]。

如果結束標籤後面緊接著換行，這個換行會被包含在結束標籤裡（也就是不會輸出）[S1.3]。

一條語句的形式是「表達式加一個分號」，例如 `$b = $a = 5;` [S5.1]。

## 範例
```php
<?php echo "Some text"; ?>
No newline
<?= "But newline now" ?>
```
輸出：
```text
Some textNo newline
But newline now
```

## 常見陷阱
- `?>` 後面的那一個換行不會輸出，所以 `Some text` 和 `No newline` 會黏在同一行 [S1.3]

## 出處
- [S1.3] https://www.php.net/manual/zh/language.basic-syntax.instruction-separation.php
- [S5.1] https://www.php.net/manual/zh/language.expressions.php
