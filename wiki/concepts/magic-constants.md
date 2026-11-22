---
title: 魔術常數（__LINE__、__FILE__…）
slug: magic-constants
sources: [S4.2]
related: [[constants]]
---
## 一句話說明
魔術常數的值會依它被使用的位置而變，例如 `__LINE__` 是它所在的行號 [S4.2]。

## 說明
所有魔術常數都在編譯時解析，一般常數則在執行時解析 [S4.2]。魔術常數不區分大小寫 [S4.2]。

常用的魔術常數 [S4.2]：
- `__LINE__`：檔案中目前的行號 [S4.2]
- `__FILE__`：檔案的完整路徑和檔名；用在被 include 的檔案中時，回傳被 include 的檔名 [S4.2]
- `__DIR__`：檔案所在的目錄，等於 `dirname(__FILE__)`；除非是根目錄，否則結尾沒有斜線 [S4.2]
- `__FUNCTION__`：目前函式的名稱，匿名函式是 `{closure}` [S4.2]
- `__CLASS__`、`__METHOD__`、`__NAMESPACE__`：目前的類別名稱、類別方法名稱、命名空間名稱 [S4.2]

## 範例
```php
<?php
function where()
{
    return __FUNCTION__ . " @ line " . __LINE__;
}
echo where(), PHP_EOL;
echo basename(__FILE__), PHP_EOL;
?>
```
輸出（PHP 8.3.6 實測）：
```text
where @ line 4
example.php
```

## 常見陷阱
- `__FILE__` 在被 include 的檔案裡是被 include 的那個檔案，而不是主程式 [S4.2]

## 出處
- [S4.2] https://www.php.net/manual/zh/language.constants.magic.php
