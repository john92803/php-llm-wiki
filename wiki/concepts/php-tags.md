---
title: PHP 標記（PHP tags）
slug: php-tags
sources: [S1.1, S1.3]
related: [[html-embedding]], [[statement-separation]]
---
## 一句話說明
PHP 只執行 `<?php` 和 `?>` 之間的程式碼，標籤外的內容會被解析器忽略 [S1.1]。

## 說明
PHP 處理檔案時，用起始標籤 `<?php` 和結束標籤 `?>` 界定 PHP 程式碼的範圍；標籤之外的內容會被 PHP 解析器忽略，所以 PHP 可以嵌入各種文件中 [S1.1]。

`<?php` 後面必須接一個空白字元（空格、tab 或換行），省略會造成語法錯誤 [S1.1]。

`<?=` 是 `<?php echo` 的簡寫（短輸出標籤）[S1.1]。

短標籤 `<?` 可以透過 `php.ini` 的 `short_open_tag` 停用；PHP 安裝時如果用了 `--disable-short-tags`，預設就是停用的 [S1.1]。因為短標籤可能被停用，建議用一般標籤 `<?php ?>` 和 `<?= ?>` 以取得最大相容性 [S1.1]。

如果檔案以 PHP 程式碼結尾，最好刪掉檔案最後的 `?>`，避免結束標籤後面意外多出空白或換行，造成不想要的輸出 [S1.1]。使用 include 或 require 時省略結尾標籤，之後仍然可以送出 header [S1.3]。

## 範例
```php
<?php
echo "Hello world\n";

// ... 更多程式碼

echo "Last statement\n";

// 腳本在這裡結束，沒有寫 PHP 結束標籤
```
輸出：
```text
Hello world
Last statement
```

## 常見陷阱
- 寫成 `<?phpecho` 這種沒有空白的寫法會語法錯誤，`<?php` 後一定要有空白 [S1.1]
- 依賴短標籤 `<?`：換一台把 `short_open_tag` 關掉的伺服器就不能用 [S1.1]
- 純 PHP 檔在結尾寫了 `?>`，後面又多一個空行，就會意外輸出空白 [S1.1][S1.3]

## 出處
- [S1.1] https://www.php.net/manual/zh/language.basic-syntax.phptags.php
- [S1.3] https://www.php.net/manual/zh/language.basic-syntax.instruction-separation.php
