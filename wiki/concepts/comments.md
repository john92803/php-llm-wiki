---
title: 註解（Comments）
slug: comments
sources: [S1.4]
related: [[php-tags]]
---
## 一句話說明
PHP 支援 C、C++ 和 Unix shell（Perl）風格的註解：`/* */`、`//`、`#` [S1.4]。

## 說明
單行註解有 `//`（C++ 風格）和 `#`（shell 風格）兩種，多行註解用 `/* */`（C 風格）[S1.4]。

單行註解只註解到行尾或目前的 PHP 程式碼區塊結束，看哪個先出現；所以 `// ... ?>` 或 `# ... ?>` 之後的 HTML 會被顯示出來 [S1.4]。

C 風格的註解遇到第一個 `*/` 就結束，所以不要巢狀使用 C 風格的註解 [S1.4]。

## 範例
```php
<?php
    echo "This is a test\n"; // 這是單行 c++ 樣式註解
    /* 這是一條多行註解
       另一行也是註解 */
    echo "This is yet another test\n";
    echo "One Final Test\n"; # 這是單行 shell 風格的註解
?>
```
輸出：
```text
This is a test
This is yet another test
One Final Test
```

```php
<h1>This is an <?php # echo 'simple';?> example</h1>
```
輸出：
```text
<h1>This is an  example</h1>
```

## 常見陷阱
- 以為 `#` 或 `//` 會把整行都註解掉：遇到 `?>` 就會跳回 HTML 模式 [S1.4]
- 用 `/* */` 註解掉一大段已經含有 `/* */` 的程式碼，會在第一個 `*/` 提早結束 [S1.4]

## 出處
- [S1.4] https://www.php.net/manual/zh/language.basic-syntax.comments.php
