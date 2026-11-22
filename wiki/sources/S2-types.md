---
id: S2
title: 類型
raw: raw/02-types.md
subpages: [S2.1, S2.2, S2.3, S2.4, S2.5, S2.6, S2.7, S2.8, S2.9]
fidelity: 9/9 verbatim
ingested: 2026-11-22
---
## 摘要
PHP 是動態型別語言，變數的型別在執行時由存放的值決定 [S2.1][S2.9]。內建型別包括 null、bool、int、float、string、array、object、callable、resource [S2.1]。當運算需要別的型別時，PHP 會依上下文自動轉換（type juggling），這是 PHP 和許多語言最大的不同 [S2.1][S2.9]。string 是位元組序列 [S2.7]，array 其實是有序映射（ordered map）[S2.8]。

## 重點
- 用 `var_dump()` 看值和型別，用 `get_debug_type()` 取得型別名稱 [S2.1]
- 轉成 bool 時 `0`、`0.0`、`""`、`"0"`、空陣列、null 都是 false，`-1` 和 `"false"` 是 true [S2.4]
- 整數溢位會變成 float；`1/2` 得到 float `0.5`，整數除法要用 `intdiv()` [S2.5]
- 浮點數不能直接比較相等，要用 epsilon [S2.6]
- 單引號不解析變數與跳脫序列，雙引號和 heredoc 會 [S2.7]
- 陣列鍵會被強制轉換（`"8"` → `8`、`true` → `1`），`unset()` 不會重建索引 [S2.8]

## 跟其他語言不同的地方
- 字串連接用 `.`，`+` 沒有連接功能 [S2.7]
- 字串 `"0"` 轉成 bool 是 false [S2.4]
- 沒有無號整數 [S2.5]；整數溢位自動變 float，不會 wrap around [S2.5]
- array 同時是 list 與 dictionary，不區分索引陣列和關聯陣列 [S2.8]
- 陣列指派預設是複製值 [S2.8]

## 相關概念
[[type-system]]、[[null]]、[[truthy-falsy]]、[[integer]]、[[float]]、[[strings]]、[[heredoc-nowdoc]]、[[string-interpolation]]、[[arrays]]、[[type-juggling]]
