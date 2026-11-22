---
title: Heredoc 與 Nowdoc
slug: heredoc-nowdoc
sources: [S2.7]
related: [[strings]], [[string-interpolation]]
---
## 一句話說明
heredoc（`<<<ID`）像沒有引號的雙引號字串，nowdoc（`<<<'ID'`）像單引號字串，適合寫多行文字 [S2.7]。

## 說明
heredoc 的寫法是 `<<<` 加一個識別字，然後換行，接著是字串內容，最後再用同一個識別字結束 [S2.7]。識別字只能包含字母、數字和底線，而且必須以字母或底線開頭 [S2.7]。

結束識別字可以用空格或 tab 縮排，這時所有內容都會刪掉相同的縮排；PHP 7.3.0 之前，結束識別字必須在該行的第一欄 [S2.7]。

結束識別字的縮排如果超過內容任何一行的縮排，會丟出 ParseError [S2.7]。縮排時 tab 和空格不能混用，否則也會丟出 ParseError [S2.7]。

heredoc 裡的單引號、雙引號都不用跳脫，但跳脫序列仍然有效，變數也會被替換 [S2.7]。

nowdoc 的識別字要用單引號括起來，例如 `<<<'EOT'`；nowdoc 不做字串插值，反斜線一律照字面處理 [S2.7]。heredoc 的所有規則（特別是結束識別字的規則）也適用於 nowdoc [S2.7]。nowdoc 是在 PHP 5.3.0 加入的 [S2.7]。

## 範例
```php
<?php
$name = 'MyName';

echo <<<EOT
    My name is "$name".
    This should print a capital 'A': \x41
    EOT;
echo PHP_EOL;
echo <<<'EOT'
    My name is "$name".
    This should not print a capital 'A': \x41
    EOT;
?>
```
輸出（PHP 8.3.6 實測）：
```text
My name is "MyName".
This should print a capital 'A': A
My name is "$name".
This should not print a capital 'A': \x41
```

## 常見陷阱
- 不要選一個會出現在內容裡的單字當結束識別字，行首出現同樣的單字可能被當成結束而造成 ParseError [S2.7]
- 結束識別字縮排比內容還深會造成 ParseError [S2.7]
- 縮排混用 tab 和空格會造成 ParseError [S2.7]

## 出處
- [S2.7] https://www.php.net/manual/zh/language.types.string.php
