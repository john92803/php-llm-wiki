---
title: 從 HTML 中分離（PHP 嵌入 HTML）
slug: html-embedding
sources: [S1.2, S1.3]
related: [[php-tags]], [[statement-separation]]
---
## 一句話說明
PHP 檔可以混合 HTML 和 PHP：標籤外的內容會原樣輸出，標籤內的才會被執行 [S1.2]。

## 說明
PHP 解析器會忽略一對開始和結束標籤之外的內容，所以 PHP 檔可以有混合內容，例如當作模板 [S1.2]。

PHP 遇到 `?>` 結束標籤時，會把後面的內容原樣輸出，直到遇到下一個開始標籤（除非緊接著換行，見 [[statement-separation]]）[S1.2]。

例外是在條件語句中間：PHP 會依照條件判斷，跳過條件沒有成立的段落，即使那段內容在 PHP 標籤之外 [S1.2]。

要輸出大段文字時，跳出 PHP 解析模式通常比用 echo 或 print 輸出更有效率 [S1.2]。

PHP 嵌入 XML 或 XHTML 時，必須使用標準的 `<?php ?>` 標籤 [S1.2]。

## 範例
```php
<p>This is going to be ignored by PHP and displayed by the browser.</p>
<?php echo 'While this is going to be parsed.'; ?>
<p>This will also be ignored by PHP and displayed by the browser.</p>
```
輸出：
```text
<p>This is going to be ignored by PHP and displayed by the browser.</p>
While this is going to be parsed.<p>This will also be ignored by PHP and displayed by the browser.</p>
```

```php
<?php $expression = true; ?>
<?php if ($expression == true): ?>
  This will show if the expression is true.
<?php else: ?>
  Otherwise this will show.
<?php endif; ?>
```
輸出：
```text
This will show if the expression is true.
```

## 常見陷阱
- 以為 `?>` 之後的 HTML 一定會輸出：放在條件語句中間的 HTML 會依條件被跳過 [S1.2]
- `?>` 後面緊接的換行會被吃掉，所以輸出可能黏在一起（上面第一個範例的第二、三行）[S1.2][S1.3]

## 出處
- [S1.2] https://www.php.net/manual/zh/language.basic-syntax.phpmode.php
- [S1.3] https://www.php.net/manual/zh/language.basic-syntax.instruction-separation.php
