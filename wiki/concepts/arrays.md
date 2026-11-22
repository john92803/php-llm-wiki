---
title: 陣列（array）——有序映射
slug: arrays
sources: [S2.5, S2.7, S2.8]
related: [[type-juggling]], [[string-interpolation]], [[null]]
---
## 一句話說明
PHP 的 array 其實是有序映射（ordered map），同一個型別可以當 list、字典、堆疊、佇列等使用 [S2.8]。

## 說明
array 是把 value 關聯到 key 的有序映射，可以當成陣列、列表（向量）、雜湊表、字典、集合、堆疊、佇列等使用 [S2.8]。

用 `array()` 或短陣列語法 `[]` 建立，內容是以逗號分隔的 `key => value` [S2.8]。key 可以是 int 或 string，value 可以是任意型別 [S2.8]。

key 會被強制轉換：內容是有效十進位整數的 string 會轉成 int（`"8"` → `8`，但 `"08"` 不會）；float 捨去小數（`8.7` → `8`）；bool 轉成 int（`true` → `1`）；null 轉成 `""`；array 和 object 不能當 key [S2.8]。多個元素使用相同 key 時，只有最後一個會保留 [S2.8]。

PHP 不區分索引陣列和關聯陣列，同一個 array 可以同時有 int 和 string 的 key [S2.8]。沒有指定 key 時，PHP 會用之前用過的最大 int key 加 1 [S2.8]。這個最大 key 不需要目前還存在於 array 中，只要在上次重建索引後曾經存在過就算 [S2.8]。

用 `$arr[key] = value` 新增或修改，用 `$arr[] = value` 附加，用 `unset()` 刪除 [S2.8]。`unset()` 不會重建索引，需要的話用 `array_values()` [S2.8]。存取未定義的 key 會發出 `E_WARNING`（PHP 8.0.0 之前是 `E_NOTICE`），結果是 `null` [S2.8]。

array 的指派總是會複製值；要共用同一份資料要用引用運算子 `&` [S2.8]。

PHP 7.1.0 起可以用 `[]` 解構（destructuring）陣列，例如 `[$a, $b] = $arr`，也可以用來交換兩個變數 [S2.8]。

array 轉成 string 一律是 `"Array"` [S2.7]。

## 範例
```php
<?php
$array = array(
    1    => "a",
    "1"  => "b",
    1.5  => "c",
    true => "d",
);
var_dump($array);

$a = array(1 => 'one', 2 => 'two', 3 => 'three');
unset($a[2]);
$a[] = 'four';
print_r($a);

$arr1 = array(2, 3);
$arr2 = $arr1;
$arr2[] = 4;
echo count($arr1), " ", count($arr2), PHP_EOL;
?>
```
輸出（PHP 8.3.6 實測）：
```text
Deprecated: Implicit conversion from float 1.5 to int loses precision in example.php on line 5
array(1) {
  [1]=>
  string(1) "d"
}
Array
(
    [1] => one
    [3] => three
    [4] => four
)
2 3
```

## 常見陷阱
- `"1"`、`1.5`、`true` 當 key 都會變成 `1`，後面的值會覆蓋前面的 [S2.8]
- 用帶小數的 float（例如 `1.5`）當 key 會被捨去小數；自 PHP 8.1.0 起這種失去精度的轉換會發出棄用通知（原文範例輸出沒有顯示這行，實測才發現）[S2.5][S2.8]
- `unset()` 之後索引會有洞，新附加的元素不會補回去 [S2.8]
- 字串 key 一定要加引號：`$foo['bar']` 而不是 `$foo[bar]`；PHP 8.0.0 起未定義常數當裸字串會丟出 Error [S2.8]
- 把 array 指派給另一個變數後修改，原本的 array 不會變（複製值）[S2.8]
- PHP 8.3.0 之前，指定負數 key `n` 後下一個 key 是 `0`；PHP 8.3.0 起是 `n+1` [S2.8]

## 出處
- [S2.5] https://www.php.net/manual/zh/language.types.integer.php
- [S2.7] https://www.php.net/manual/zh/language.types.string.php
- [S2.8] https://www.php.net/manual/zh/language.types.array.php
