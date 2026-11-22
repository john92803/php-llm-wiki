---
title: 字串（string）與單／雙引號
slug: strings
sources: [S2.7, S2.9]
related: [[string-interpolation]], [[heredoc-nowdoc]], [[type-juggling]]
---
## 一句話說明
PHP 的 string 是一串位元組；單引號幾乎不做任何處理，雙引號會解析跳脫序列和變數 [S2.7]。

## 說明
string 由一系列字元組成，每個字元等於一個位元組，所以 PHP 只支援 256 個字元的字元集，原生不支援 Unicode [S2.7]。PHP 內部的 string 是位元組陣列加上一個長度，沒有獨立的 byte 型別 [S2.7]。

字串有 4 種寫法：單引號、雙引號、heredoc、nowdoc [S2.7]。

單引號字串中，只有 `\'`（單引號）和 `\\`（反斜線）需要跳脫，其他反斜線都是字面上的反斜線；`\n` 不代表換行，變數也不會被替換 [S2.7]。

雙引號字串會解析跳脫序列，例如 `\n`、`\t`、`\\`、`\$`、`\"`、`\x41`、`\u{41}` [S2.7]。雙引號字串最重要的特徵是變數會被解析，見 [[string-interpolation]] [S2.7]。

字串連接用 `.`（點）運算子，`+`（加號）沒有這個功能 [S2.7]。

字串中的字元可以用從 0 開始的下標存取和修改，例如 `$str[0]` [S2.7]。PHP 7.1.0 起支援負的偏移量，從字串尾端算起 [S2.7]。用大括號存取（`$str{42}`）自 PHP 7.4.0 起棄用、PHP 8.0.0 起不再支援 [S2.7]。下標是依位元組運作的，對多位元組字元集不安全 [S2.7]。

值轉成 string：`true` 變 `"1"`、`false` 變 `""`、`null` 變 `""`、array 一律變 `"Array"` [S2.7]。可以用 `(string)`、`strval()`，或把變數放進雙引號 [S2.7][S2.9]。

## 範例
```php
<?php
$name = 'PHP';
echo 'Hello $name\n', PHP_EOL;
echo "Hello $name\n";
echo 'Arnold once said: "I\'ll be back"', PHP_EOL;
echo "1" + "1", PHP_EOL;
echo "1" . "1", PHP_EOL;
$s = 'string';
echo $s[0], $s[-1], PHP_EOL;
?>
```
輸出（PHP 8.3.6 實測）：
```text
Hello $name\n
Hello PHP
Arnold once said: "I'll be back"
2
11
sg
```

## 常見陷阱
- 想連接字串卻寫成 `+` [S2.7]
- 在單引號裡寫 `\n` 或 `$var`，以為會換行或代入變數 [S2.7]
- `strlen()`、下標都是以位元組計算，處理 UTF-8 中文要小心 [S2.7]
- `echo` 一個陣列只會印出 `Array` [S2.7]

## 出處
- [S2.7] https://www.php.net/manual/zh/language.types.string.php
- [S2.9] https://www.php.net/manual/zh/language.types.type-juggling.php
