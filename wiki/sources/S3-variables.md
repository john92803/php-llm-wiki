---
id: S3
title: 變數
raw: raw/03-variables.md
subpages: [S3.1, S3.2, S3.3, S3.4]
fidelity: 4/4 verbatim
ingested: 2026-11-22
---
## 摘要
PHP 的變數用 `$` 加名稱表示，名稱區分大小寫 [S3.1]。指派預設是傳值，加 `&` 才是引用 [S3.1]。函式內看不到全域變數，必須用 `global` 或 `$GLOBALS` [S3.2]。`static` 變數在函式呼叫之間保留值 [S3.2]。變數名稱可以動態決定（可變變數，`$$a`）[S3.3]，另外有在每個作用域都自動可用的超全域變數 [S3.4]。

## 重點
- 變數名稱以字母或底線開頭，區分大小寫 [S3.1]
- 預設傳值指派；`$b = &$a` 是引用指派 [S3.1]
- 存取未定義變數：`E_WARNING`（PHP 8.0.0 之前是 `E_NOTICE`），值為 null [S3.1]
- 函式內不會自動看到全域變數 [S3.2]
- `static` 變數只在第一次呼叫時初始化 [S3.2]

## 跟其他語言不同的地方
- 變數一定要加 `$` [S3.1]
- 跟 C 不同，全域變數不會自動提供給函式，要宣告 `global` [S3.2]
- PHP 只有函式作用域和全域作用域 [S3.2]

## 相關概念
[[variables]]、[[variable-scope]]、[[variable-variables]]、[[superglobals]]
