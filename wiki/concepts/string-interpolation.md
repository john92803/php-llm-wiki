---
title: 字串插值（String Interpolation）
slug: string-interpolation
sources: [S2.7, S2.8]
related: [[strings]], [[heredoc-nowdoc]], [[arrays]], [[variable-variables]]
---
## 一句話說明
雙引號字串和 heredoc 中的 `$變數` 會被替換成值；複雜的運算式要用 `{$...}` 包起來 [S2.7]。

## 說明
字串用雙引號或 heredoc 定義時，其中的變數會被替換；語法分成基本語法和進階（大括號）語法 [S2.7]。

基本語法：遇到 `$` 時，後面的字元會被解釋為變數名稱，然後替換為變數的值 [S2.7]。基本語法可以插入變數、陣列的第一維（例如 `$juices[0]`、`$juices[string_key]`）或物件屬性（`$o->s`）[S2.7]。如果 `$` 後面無法形成有效的變數名稱，`$` 會保持原樣 [S2.7]。

進階語法：把運算式用 `{` 和 `}` 包起來，可以插入任意的純量變數、陣列元素或物件屬性 [S2.7]。因為 `{` 無法跳脫，只有 `$` 緊接在 `{` 後面時才會被識別，`{ $great}` 不會插值 [S2.7]。

`${ expression }` 語法從 PHP 8.2.0 開始被棄用 [S2.7]。

在雙引號字串裡寫 `"$arr['fruit']"` 會造成解析錯誤，要改寫成 `"{$arr['fruit']}"` [S2.8]。

## 範例
```php
<?php
$juice = "apple";
$juices = array("apple", "orange", "string_key" => "purple");
$arr = ['fruit' => 'banana'];

echo "He drank some $juice juice." . PHP_EOL;
echo "He drank some $juices[string_key] juice." . PHP_EOL;
echo "This works: {$arr['fruit']}" . PHP_EOL;
echo "This is { $juice}" . PHP_EOL;
?>
```
輸出（PHP 8.3.6 實測）：
```text
He drank some apple juice.
He drank some purple juice.
This works: banana
This is { apple}
```

## 常見陷阱
- `{` 和 `$` 之間有空格就不會插值 [S2.7]
- 在雙引號裡用帶引號的鍵 `"$arr['key']"` 是解析錯誤，要加大括號 [S2.8]
- 不要再用 `"${var}"`，PHP 8.2.0 起棄用，改用 `"{$var}"` [S2.7]

## 出處
- [S2.7] https://www.php.net/manual/zh/language.types.string.php
- [S2.8] https://www.php.net/manual/zh/language.types.array.php
