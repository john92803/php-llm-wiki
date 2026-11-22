# S2 類型（raw）

- 章節：`language.types`
- 取得方式：curl 下載 https://www.php.net/manual/zh/<頁面>.php 原始 HTML → 擷取 `div#<頁面ID>` 正文 → 排除 User Contributed Notes → pandoc 轉 Markdown（tools/fetch_raw.py）
- 抓取日期：2026-11-22
- 本檔為官方手冊原文（簡體中文），不可修改。

---

## [S2.1] 簡介

- url: https://www.php.net/manual/zh/language.types.intro.php
- fidelity: verbatim
- fetched: 2026-11-22

## 简介

PHP 中的每个表达式都属于以下某个内置类型，具体取决于值：

- null

- bool

- int

- float（浮点数）

- string

- array

- object

- callable

- resource

PHP 是动态类型语言，这意味着默认不需要指定变量的类型，因为会在运行时确定。然而，可以通过使用类型声明对语言的一些方面进行类型静态化。可以在类型系统页面找到 PHP 类型系统支持的不同类型。

类型限制了可以对其执行的操作。然而，如果使用的表达式/变量不支持该操作，PHP 将尝试将该值类型转换为操作支持的类型。此过程取决于使用该值的上下文。更多信息参阅类型转换。

**小技巧**

类型比较表也很有用，因为存在不同类型之间的值的各种比较示例。

> **注意**:
>
> 使用类型转换，强制将表达式的值转换为某种类型。还可以使用 settype() 函数就地对变量进行类型转换。

要检查表达式的值和类型，请使用 var_dump()函数。要获取表达式的类型，请使用 get_debug_type()函数。不过，要检查表达式是否属于某种类型，请改用 `is_``type`函数。

**示例 \#1 不同类型**

``` php
<?php
$a_bool = true;   // a bool
$a_str  = "foo";  // a string
$a_str2 = 'foo';  // a string
$an_int = 12;     // an int
echo get_debug_type($a_bool), "\n";
echo get_debug_type($a_str), "\n";

// 如果是整型，就加上 4
if (is_int($an_int)) {
    $an_int += 4;
}
var_dump($an_int);

// 如果 $a_bool 是字符串，就打印出来
if (is_string($a_bool)) {
    echo "String: $a_bool";
}
?>
```

以上示例在 PHP 8 中的输出：

    bool
    string
    int(16)

> **注意**:
>
> PHP 8.0.0 之前，get_debug_type() 无效，可以使用 gettype() 函数代替。但是没有使用规范的类型名称。

---

## [S2.2] 型別系統

- url: https://www.php.net/manual/zh/language.types.type-system.php
- fidelity: verbatim
- fetched: 2026-11-22

## 类型系统

PHP 采用名义类型系统，并具有强行为的子类型关系。子类型关系在编译时检查，而类型验证则在运行时动态进行。

PHP 的类型系统支持各种原子类型，可以组合在一起创建更加复杂的类型。其中一些类型可以写成类型声明。

### 原子类型

一些原子类型是内置类型，跟语言紧密集成，不能用用户定义类型重现（reproduced）。

基础类型列表是：

- 内置类型

  - 标量类型：

    - bool 类型

    - int 类型

    - float 类型

    - string 类型

  - array 类型

  - object 类型

  - resource 类型

  - never 类型

  - void 类型

  - 相对类类型：self、parent 和 static

  - 单例类型

    - false

    - true

  - 单值类型

    - null

- 用户定义的类型（通常称为类类型）

  - 接口

  - 类

  - 枚举

- callable 类型

#### 标量类型

如果值是 int、float、string 或 bool 类型，则视该值为标量。

#### 用户定义类型

可以使用 interface、类和枚举定义自定义类型。这些被视为用户定义类型或类类型。例如，可以定义名为 `Elephant` 的类，然后可以实例化 `Elephant` 类型的对象，并且函数可以请求 `Elephant` 类型的参数。

### 复合类型

可以将多个原子类型组合为复合类型。PHP 允许使用以下方式组合类型：

- 类类型（接口和类名）的交集。

- 类型联合。

#### 交集类型

交集类型接受满足多个类类型声明的值，而不是单个值。交集类型中的每个类型由 `&` 符号连接。因此，类型 `T`、`U` 和 `V` 组成的交集类型将写成 `T&U&V`。

#### 联合类型

联合类型接受多个不同类型的值，而不是单个类型。联合类型中的每个类型由 `|` 符号连接。因此类型 `T`、`U` 和 `V` 的联合类型写成 `T|U|V`。如果其中一种类型是交集类型，需要使用括号括起来，在 DNF 中写成：`T|(X&Y)`。

### 类型别名

PHP 支持两种类型别名 mixed 和 iterable，分别对应 `object|resource|array|string|float|int|bool|null` 和 `Traversable|array` 的联合类型。

> **注意**:
>
> PHP 不支持用户定义类型别名。

---

## [S2.3] NULL

- url: https://www.php.net/manual/zh/language.types.null.php
- fidelity: verbatim
- fetched: 2026-11-22

## NULL

null 类型是 PHP 的原子类型（unit type），也就是说，它仅有一个值 **`null`**。

未定义和 unset() 的变量都将解析为值 **`null`**。

### 语法

**`null`** 类型只有一个值，就是不区分大小写的常量 **`null`**。

``` php
<?php
$var = NULL;       
?>
```

### 转换到 **`null`**

**警告**

本特性自 PHP 7.2.0 起*废弃*，并且自 PHP 8.0.0 起被*移除*。 强烈建议不要使用本特性。

使用 `(unset) $var` 将一个变量转换为 null 将*不会*删除该变量或 unset 其值。仅是返回 **`null`** 值而已。

### 参见

- is_null()
- unset()

---

## [S2.4] Boolean

- url: https://www.php.net/manual/zh/language.types.boolean.php
- fidelity: verbatim
- fetched: 2026-11-22

## Boolean 布尔类型

bool 仅有两个值，用于表达真（truth）值，不是 **`true`** 就是 **`false`**。

### 语法

要指定一个 bool，使用常量 **`true`** 或 **`false`**。两个都不区分大小写。

``` php
<?php
$foo = True; // 设置 $foo 为 TRUE
?>
```

通常运算符所返回的 bool 值结果会被传递给控制流程。

``` php
<?php
$action = "show_version";
$show_separators = true;

// == 是一个操作符，它检测两个变量是否相等，并返回一个布尔值
if ($action == "show_version") {
    echo "The version is 1.23";
}

// 这样做是不必要的...
if ($show_separators == TRUE) {
    echo "<hr>\n";
}

// ...因为可以使用下面这种简单的方式：
if ($show_separators) {
    echo "<hr>\n";
}
?>
```

### 转换为布尔值

要明确地将值转换成 bool，可以用 `(bool)` 强制转换。通常这不是必需的，因为值在逻辑上下文中使用将会自动解释为 bool 类型的值。更多信息请阅读类型转换页面。

参见类型转换的判别。

当转换为 bool 时，以下值被认为是 **`false`**：

- 布尔值 **`false`** 本身

- 整型值 `0`（零）

- 浮点型值 `0.0`（零）`-0.0`（零）

- 空字符串 `""`，以及字符串 `"0"`

- 不包括任何元素的数组

- 原子类型 NULL（包括尚未赋值的变量）

- 内部对象的强制转换行为重载为 bool。例如：由不带属性的空元素创建的 SimpleXML 对象。

所有其它值都被认为是 **`true`**（包括 资源 和 **`NAN`**）。

**警告**

`-1` 和其它非零值（不论正负）一样，被认为是 **`true`**！

**示例 \#1 转换为布尔型**

``` php
<?php
var_dump((bool) "");        // bool(false)
var_dump((bool) "0");       // bool(false)
var_dump((bool) 1);         // bool(true)
var_dump((bool) -2);        // bool(true)
var_dump((bool) "foo");     // bool(true)
var_dump((bool) 2.3e5);     // bool(true)
var_dump((bool) array(12)); // bool(true)
var_dump((bool) array());   // bool(false)
var_dump((bool) "false");   // bool(true)
?>
```

---

## [S2.5] Integer

- url: https://www.php.net/manual/zh/language.types.integer.php
- fidelity: verbatim
- fetched: 2026-11-22

## Integer 整型

int 是集合 ℤ = {..., -2, -1, 0, 1, 2, ...} 中的某个数。

### 参见

- 浮点数
- 任意精度/BCMath
- 任意长度整数/GMP

### 语法

Int 可以使用十进制，十六进制，八进制或二进制表示，前面可以加上可选的符号（- 或者 +）。 可以用负运算符 来表示一个负的 int。

要使用八进制表达，数字前必须加上 `0`（零）。 PHP 8.1.0 起，八进制表达也可以在前面加上 `0o` 或者 `0O` 。 要使用十六进制表达，数字前必须加上 `0x`。要使用二进制表达，数字前必须加上 `0b`。

从 PHP 7.4.0 开始，为了提升字面量的可读性，整型数值可以包含下划线 (`_`)。PHP 扫描器会移除这些下划线。

**示例 \#1 整数文字表达**

``` php
<?php
$a = 1234; // 十进制数
$a = 0123; // 八进制数 (等于十进制 83)
$a = 0o123; // 八进制数 (PHP 8.1.0 起)
$a = 0x1A; // 十六进制数 (等于十进制 26)
$a = 0b11111111; // 二进制数字 (等于十进制 255)
$a = 1_234_567; // 整型数值 (PHP 7.4.0 以后)
?>
```

int literal 的结构形式从 PHP 8.1.0 开始是（之前不允许使用 `0o` 或 `0O` 八进制前缀，并且 PHP 7.4.0 之前不允许使用下划线）：

    decimal     : [1-9][0-9]*(_[0-9]+)*
                | 0

    hexadecimal : 0[xX][0-9a-fA-F]+(_[0-9a-fA-F]+)*

    octal       : 0[oO]?[0-7]+(_[0-7]+)*

    binary      : 0[bB][01]+(_[01]+)*

    integer     : decimal
                | hexadecimal
                | octal
                | binary

整型数 int 的字长和平台有关，尽管通常最大值是大约二十亿（32 位有符号）。64 位平台下的最大值通常是大约 9E18。 PHP 不支持无符号的 int。int 值的字长可以用常量 **`PHP_INT_SIZE`**来表示， 最大值可以用常量 **`PHP_INT_MAX`** 来表示， 最小值可以用常量 **`PHP_INT_MIN`** 表示。

### 整数溢出

如果给定的一个数超出了 int 的范围，将会被解释为 float。同样如果执行的运算结果超出了 int 范围，也会返回 float。

**示例 \#2 整数溢出**

``` php
<?php
$large_number = 50000000000000000000;
var_dump($large_number);         // float(5.0E+19)
var_dump(PHP_INT_MAX + 1);       // 32 位系统：float(2147483648)
                                 // 64 位系统：float(9.2233720368548E+18)
?>
```

### 整数除法

PHP 没有 int 除法取整运算符，要使用 intdiv() 实现。 `1/2` 产生出 float `0.5`。 值可以舍弃小数部分，强制转换为 int，或者使用 round() 函数可以更好地进行四舍五入。

**示例 \#3 Divisions**

``` php
<?php
var_dump(25/7);         // float(3.5714285714286) 
var_dump((int) (25/7)); // int(3)
var_dump(round(25/7));  // float(4) 
?>
```

### 转换为整型

要明确地将一个值转换为 int，用 `(int)` 强制转换。 不过大多数情况下都不需要强制转换，因为当运算符，函数或流程控制需要一个 int 参数时，值会自动转换。还可以通过函数 intval() 来将一个值转换成 int 整型。

将 resource 转换成 int 时， 结果会是 PHP 运行时为 resource 分配的唯一资源号。

参见：类型转换的判别。

#### 从布尔值转换

**`false`** 将产生出 `0`（零），**`true`** 将产生出 `1`（壹）。

#### 从浮点型转换

当从浮点数 float 转换成整数 int时，将*向零*取整。自 PHP 8.1.0 起，当将非整数类型的 float 转换为失去精度的 int 时，会发出弃用通知。

**示例 \#4 从浮点数转换**

``` php
<?php

function foo($value): int {
  return $value; 
}

var_dump(foo(8.1)); // 自 PHP 8.1.0 起：“Deprecated: Implicit conversion from float 8.1 to int loses precision”
var_dump(foo(8.1)); // PHP 8.1.0 之前为 8
var_dump(foo(8.0)); // 均为 8

var_dump((int) 8.1); // 均为 8
var_dump(intval(8.1)); // 均为 8
?>
```

如果浮点数超出了 int 范围（32 位平台下通常为 `+/- 2.15e+9 = 2^31`，64 位平台下，通常为 `+/- 9.22e+18 = 2^63`），则结果为未定义， 因为没有足够的精度给出一个确切的 int 结果。 在此情况下没有警告，甚至没有任何通知！

> **注意**:
>
> `NaN`、`Inf` 和 `-Inf` 在转换成 int 时是零。

**警告**

绝不要将未知的分数强制转换为 int，这样有时会导致不可预料的结果。

``` php
<?php
echo (int) ( (0.1+0.7) * 10 ); // 显示 7!
?>
```

参见关于浮点数精度的警告。

#### 从字符串转换

如果 string 是 numeric 或者前导数字， 则将它解析为相应的 int 值，否则将转换为零（`0`）。

#### 从 NULL 转换

**`null`** 会转换为零（`0`）。

#### 从其它类型转换

**警告**

没有定义从其它类型转换为 int 的行为。 *不要*依赖任何现有的行为，因为它会未加通知地改变。

---

## [S2.6] Float

- url: https://www.php.net/manual/zh/language.types.float.php
- fidelity: verbatim
- fetched: 2026-11-22

## Float 浮点型

浮点型（也叫浮点数 float，双精度数 double 或实数 real）可以用以下任一语法定义：

``` php
<?php
$a = 1.234; 
$b = 1.2e3; 
$c = 7E-10;
$d = 1_234.567; // 从 PHP 7.4.0 开始支持
?>
```

浮点数的形式表示（PHP 7.4.0 之前不支持下划线）：

    LNUM          [0-9]+(_[0-9]+)*
    DNUM ({LNUM}?"."{LNUM}) | ({LNUM}"."{LNUM}?)
    EXPONENT_DNUM (({LNUM} | {DNUM}) [eE][+-]? {LNUM})

浮点数的字长和平台相关，尽管通常最大值是 1.8e308 并具有 14 位十进制数字的精度（64 位 IEEE 格式）。

**警告**

# 浮点数的精度

浮点数的精度有限。尽管取决于系统，PHP 通常使用 IEEE 754 双精度格式，则由于取整而导致的最大相对误差为 1.11e-16。非基本数学运算可能会给出更大误差，并且要考虑到进行复合运算时的误差传递。

此外，以十进制能够精确表示的有理数如 `0.1` 或 `0.7`，无论有多少尾数都不能被内部所使用的二进制精确表示，因此不能在不丢失一点点精度的情况下转换为二进制的格式。这就会造成混乱的结果：例如，`floor((0.1+0.7)*10)` 通常会返回 `7` 而不是预期中的 `8`，因为该结果内部的表示其实是类似 `7.9999999999999991118...`。

所以永远不要相信浮点数结果精确到了最后一位，也永远不要比较两个浮点数是否相等。如果确实需要更高的精度，应该使用任意精度数学函数或者 gmp 函数。

参见» 浮点数指南网页的简单解释。

### 转换为浮点数

#### 从 string 转换

如果 string 是 numeric 或者前导数字， 则将它解析为相应的 float 值，否则将转换为零（`0`）。

#### 从其他类型转换

对于其它类型的值，其情况类似于先将值转换成 int，然后再转换成 float。 请参阅“转换为整型”一节以获取更多信息。

> **注意**:
>
> 某些类型在转换成 int 时有未定义行为，转换为 float 时也会如此。

### 比较浮点数

如上述警告信息所言，由于内部表达方式的原因，比较两个浮点数是否相等是有问题的。不过还是有迂回的方法来比较浮点数值的。

要测试浮点数是否相等，要使用一个仅比该数值大一丁点的最小误差值。该值也被称为机器极小值（epsilon）或最小单元取整数，是计算中所能接受的最小的差别值。

`$a` 和 `$b` 在小数点后五位精度内都是相等的。

**示例 \#1 浮点比较**

``` php
<?php
$a = 1.23456789;
$b = 1.23456780;
$epsilon = 0.00001;

if (abs($a - $b) < $epsilon) {
    echo "true";
}
?>
```

### NaN

某些数学运算会产生一个由常量 **`NAN`** 所代表的结果。此结果代表着一个在浮点数运算中未定义或不可表述的值。任何拿此值与其它任何值（除了 **`true`**）进行的松散或严格比较的结果都是 **`false`**。

由于 **`NAN`** 代表着任何不同值，不应拿 **`NAN`** 去和其它值进行比较，包括其自身，应该用 is_nan() 来检查。

---

## [S2.7] String

- url: https://www.php.net/manual/zh/language.types.string.php
- fidelity: verbatim
- fetched: 2026-11-22

## String 字符串

一个字符串 string 就是由一系列的字符组成，其中每个字符等同于一个字节。这意味着 PHP 只能支持 256 的字符集，因此不支持 Unicode 。详见字符串类型详解。

> **注意**:
>
> 在 32 位版本中，string 最大可以达到 2GB（最多 2147483647 字节）。

### 语法

一个字符串可以用 4 种方式表达：

- 单引号

- 双引号

- heredoc 语法结构

- nowdoc 语法结构

#### 单引号

定义一个字符串的最简单的方法是用单引号把它包围起来（字符 `'`）。

要表达一个单引号自身，需在它的前面加个反斜线（`\`）来转义。要表达一个反斜线自身，则用两个反斜线（`\\`）。其它任何方式的反斜线都会被当成反斜线本身：也就是说如果想使用其它转义序列例如 `\r` 或者 `\n`，并不代表任何特殊含义，就单纯是这两个字符本身。

> **注意**:
>
> 不像双引号和 heredoc 语法结构，在单引号字符串中的变量和特殊字符的转义序列将*不会*被替换。

**示例 \#1 Syntax Variants**

``` php
<?php
echo 'this is a simple string', PHP_EOL;

// 可以录入多行
echo 'You can also have embedded newlines in
strings this way as it is
okay to do', PHP_EOL;

// 输出：Arnold once said: "I'll be back"
echo 'Arnold once said: "I\'ll be back"', PHP_EOL;

// 输出：You deleted C:\*.*?
echo 'You deleted C:\\*.*?', PHP_EOL;

// 输出：You deleted C:\*.*?
echo 'You deleted C:\*.*?', PHP_EOL;

// 输出：This will not expand: \n a newline
echo 'This will not expand: \n a newline', PHP_EOL;

// 输出：Variables do not $expand $either
echo 'Variables do not $expand $either', PHP_EOL;
?>
```

#### 双引号

如果字符串是包围在双引号（`"`)）中， PHP 将对以下特殊的字符进行解析：

| 序列                 | 含义                                                                                                                                                     |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `\n`                 | 换行（ASCII 字符集中的 LF 或 0x0A (10)）                                                                                                                 |
| `\r`                 | 回车（ASCII 字符集中的 CR 或 0x0D (13)）                                                                                                                 |
| `\t`                 | 水平制表符（ASCII 字符集中的 HT 或 0x09 (9)）                                                                                                            |
| `\v`                 | 垂直制表符（ASCII 字符集中的 VT 或 0x0B (11)）                                                                                                           |
| `\e`                 | Escape（ASCII 字符集中的 ESC 或 0x1B (27)）                                                                                                              |
| `\f`                 | 换页（ASCII 字符集中的 FF 或 0x0C (12)）                                                                                                                 |
| `\\`                 | 反斜线                                                                                                                                                   |
| `\$`                 | 美元标记                                                                                                                                                 |
| `\"`                 | 双引号                                                                                                                                                   |
| `\[0-7]{1,3}`        | 八进制：匹配正则表达式序列 `[0-7]{1,3}` 的是八进制表示法的字符序列（比如 `"\101" === "A"`），会静默溢出以适应一个字节（例如 `"\400" === "\000"`）        |
| `\x[0-9A-Fa-f]{1,2}` | 十六进制：匹配正则表达式序列 `[0-9A-Fa-f]{1,2}` 的是十六进制表示法的一个字符（比如 `"\x41" === "A"`）                                                    |
| `\u{[0-9A-Fa-f]+}`   | Unicode：匹配正则表达式 `[0-9A-Fa-f]+` 的字符序列是 unicode 码位，该码位能作为 UTF-8 的表达方式输出字符串。序列中必须包含大括号。例如 `"\u{41}" === "A"` |

**转义字符**

和单引号字符串一样，转义任何其它字符都会导致反斜线被显示出来。

用双引号定义的字符串最重要的特征是变量会被解析，详见变量插值。

#### Heredoc 结构

第三种表达字符串的方法是用 heredoc 句法结构：`<<<`。在该运算符之后要提供一个标识符，然后换行。接下来是字符串 string 本身，最后要用前面定义的标识符作为结束标志。

结束标识符可以使用空格或制表符（tab）缩进，此时文档字符串会删除所有缩进。 在 PHP 7.3.0 之前的版本中，结束时所引用的标识符*必须*在该行的第一列。

而且，标识符的命名也要像其它标签一样遵守 PHP 的规则：只能包含字母、数字和下划线，并且必须以字母和下划线作为开头。

**示例 \#2 PHP 7.3.0 之后的基础 Heredoc 示例**

``` php
<?php
// 无缩进
echo <<<END
      a
     b
    c
\n
END;
// 4 空格缩进
echo <<<END
      a
     b
    c
    END;
```

以上示例在 PHP 7.3 中的输出：

          a
         b
        c
      a
     b
    c

如果结束标识符的缩进超过内容的任何一行的缩进，则将抛出 ParseError 异常：

**示例 \#3 结束标识符的缩进不能超过正文的任何一行**

``` php
<?php
echo <<<END
  a
 b
c
   END;
```

以上示例在 PHP 7.3 中的输出：

    Parse error: Invalid body indentation level (expecting an indentation level of at least 3) in example.php on line 4

制表符也可以缩进结束标识符，但是，关于缩进结束标识符和内容， 制表符和空格*不能*混合使用。在以上任何情况下， 将会抛出 ParseError 异常。 之所以包含这些空白限制，是因为混合制表符和空格来缩进不利于易读性。

**示例 \#4 内容（空白）和结束标识符的不同缩进**

``` php
<?php
// 以下所有代码都不起作用。
// 正文（空格）和结束标记（制表符），不同的缩进
{
    echo <<<END
     a
        END;
}
// 在正文中混合空格和制表符
{
    echo <<<END
        a
     END;
}
// 在结束标记中混合空格和制表符
{
    echo <<<END
          a
         END;
}
```

以上示例在 PHP 7.3 中的输出：

    Parse error: Invalid indentation - tabs and spaces cannot be mixed in example.php line 8

内容字符串的结束标识符后面不需要跟分号或者换行符。 例如，从 PHP 7.3.0 开始允许以下代码：

**示例 \#5 在结束标识符后继续表达式**

``` php
<?php
$values = [<<<END
a
  b
    c
END, 'd e f'];
var_dump($values);
```

以上示例在 PHP 7.3 中的输出：

    array(2) {
      [0] =>
      string(11) "a
      b
        c"
      [1] =>
      string(5) "d e f"
    }

**警告**

如果在某一行的开头找到了结束标识符，那么不管它是否是另外一个单词的一部分， 它都可能看作结束标识符并引起 ParseError。

**示例 \#6 字符串内容中的结束标识符往往会导致 ParseError**

``` php
<?php
$values = [<<<END
a
b
END ING
END, 'd e f'];
```

以上示例在 PHP 7.3 中的输出：

    Parse error: syntax error, unexpected identifier "ING", expecting "]" in example.php on line 5

为了避免这个问题，遵循以下简单的规则较为安全： *不要选择一个出现在文本主体中的单词作为结束标识符*。

**警告**

在 PHP 7.3.0 之前，请务必注意，带有结束标识符的行不能包含除 (`;`)外的任何其他字符。 这意味着标识符*不能缩进*，分号的前后也不能有任何空白或制表符。更重要的是结束标识符的前面必须是个被本地操作系统认可的换行，比如在 UNIX 和 macOS 系统中是 `\n`，而结束定界符之后也必须紧跟一个换行。

如果不遵守该规则导致结束标识不“干净”，PHP 将认为它不是结束标识符而继续寻找。如果在文件结束前也没有找到一个正确的结束标识符，PHP 将会在最后一行产生一个解析错误。

**示例 \#7 PHP 7.3.0 之前的错误示例**

``` php
<?php
class foo {
    public $bar = <<<EOT
bar
    EOT;
}
// 不能缩进标识符
?>
```

**示例 \#8 在 PHP 7.3.0 之前有效示例**

``` php
<?php
class foo {
    public $bar = <<<EOT
bar
EOT;
}
?>
```

Heredocs 结构不能用来初始化类的属性。

Heredoc 结构就象是没有双引号的 string，这就是说在 heredoc 结构中单引号不用被转义，但是上文中列出的转义序列还可以使用。变量将被替换，但在 heredoc 结构中含有复杂的变量时要像 string 一样格外小心。

**示例 \#9 Heredoc 结构的字符串示例**

``` php
<?php
$str = <<<EOD
Example of string
spanning multiple lines
using heredoc syntax.
EOD;

/* 含有变量的更复杂示例 */
class foo
{
    var $foo;
    var $bar;

    function __construct()
    {
        $this->foo = 'Foo';
        $this->bar = array('Bar1', 'Bar2', 'Bar3');
    }
}

$foo = new foo();
$name = 'MyName';

echo <<<EOT
My name is "$name". I am printing some $foo->foo.
Now, I am printing some {$foo->bar[1]}.
This should print a capital 'A': \x41
EOT;
?>
```

以上示例会输出：

    My name is "MyName". I am printing some Foo.
    Now, I am printing some Bar2.
    This should print a capital 'A': A

也可以把 Heredoc 结构用在函数参数中来传递数据：

**示例 \#10 Heredoc 结构在参数中的示例**

``` php
<?php
var_dump(array(<<<EOD
foobar!
EOD
));
?>
```

可以用 Heredoc 结构来初始化静态变量和类的属性和常量：

**示例 \#11 使用 Heredoc 结构来初始化静态值**

``` php
<?php
// 静态变量
function foo()
{
    static $bar = <<<LABEL
Nothing in here...
LABEL;
}

// 类的常量、属性
class foo
{
    const BAR = <<<FOOBAR
Constant example
FOOBAR;

    public $baz = <<<FOOBAR
Property example
FOOBAR;
}
?>
```

还可以在 Heredoc 结构中用双引号来声明标识符：

**示例 \#12 在 heredoc 结构中使用双引号**

``` php
<?php
echo <<<"FOOBAR"
Hello World!
FOOBAR;
?>
```

#### Nowdoc 结构

就象 heredoc 结构类似于双引号字符串，Nowdoc 结构是类似于单引号字符串的。Nowdoc 结构很象 heredoc 结构，但是 nowdoc 中*不进行字符串插值*。这种结构很适合用于嵌入 PHP 代码或其它大段文本而无需对其中的特殊字符进行转义。与 SGML 的 `<![CDATA[ ]]>` 结构是用来声明大段的不用解析的文本类似，nowdoc 结构也有相同的特征。

一个 nowdoc 结构也用和 heredocs 结构一样的标记 `<<<`， 但是跟在后面的标识符要用单引号括起来，即 `<<<'EOT'`。Heredoc 结构的所有规则也同样适用于 nowdoc 结构，尤其是结束标识符的规则。

**示例 \#13 Nowdoc 结构字符串示例**

``` php
<?php
echo <<<'EOD'
Example of string spanning multiple lines
using nowdoc syntax. Backslashes are always treated literally,
e.g. \\ and \'.
EOD;
```

以上示例会输出：

    Example of string spanning multiple lines
    using nowdoc syntax. Backslashes are always treated literally,
    e.g. \\ and \'.

**示例 \#14 含变量引用的 Nowdoc 字符串示例**

``` php
<?php

/* 含有变量的更复杂的示例 */
class foo
{
    public $foo;
    public $bar;

    function __construct()
    {
        $this->foo = 'Foo';
        $this->bar = array('Bar1', 'Bar2', 'Bar3');
    }
}

$foo = new foo();
$name = 'MyName';

echo <<<'EOT'
My name is "$name". I am printing some $foo->foo.
Now, I am printing some {$foo->bar[1]}.
This should not print a capital 'A': \x41
EOT;
?>
```

以上示例会输出：

    My name is "$name". I am printing some $foo->foo.
    Now, I am printing some {$foo->bar[1]}.
    This should not print a capital 'A': \x41

**示例 \#15 静态数据的示例**

``` php
<?php
class foo {
    public $bar = <<<'EOT'
bar
EOT;
}
?>
```

> **注意**:
>
> Nowdoc 结构是在 PHP 5.3.0 中加入的。

#### 字符串插值

当字符串用双引号或 heredoc 结构定义时，其中的变量可以进行替换。

这里共有两种语法规则：一种基本规则，一种高级规则。基本的语法规则是最常用和最方便的，它可以用最少的代码在一个 string 中嵌入一个变量，一个 array 的值，或一个 object 的属性。

##### 基本语法

如果遇到一个美元符号（`$`），后面的字符会被解释为变量名，然后替换为变量的值。

**示例 \#16 String Interpolation**

``` php
<?php
$juice = "apple";

echo "He drank some $juice juice." . PHP_EOL;

?>
```

以上示例会输出：

    He drank some apple juice.

从形式上讲，基本变量替换语法的结构如下：

    string-variable::
         variable-name   (offset-or-property)?
       | ${   expression   }

    offset-or-property::
         offset-in-string
       | property-in-string

    offset-in-string::
         [   name   ]
       | [   variable-name   ]
       | [   integer-literal   ]

    property-in-string::
         ->  name

    variable-name::
         $   name

    name::
         [a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*

**警告**

`${ expression }` 语法从 PHP 8.2.0 开始被弃用，因为它可能被解释为 可变变量：

``` php
<?php
const foo = 'bar';
$foo = 'foo';
$bar = 'bar';
var_dump("${foo}");
var_dump("${(foo)}");
?>
```

以上示例在 PHP 8.2 中的输出：

    Deprecated: Using ${var} in strings is deprecated, use {$var} instead in file on line 6

    Deprecated: Using ${expr} (variable variables) in strings is deprecated, use {${expr}} instead in file on line 9
    string(3) "foo"
    string(3) "bar"

以上示例会输出：

    string(3) "foo"
    string(3) "bar"

高级 字符串插值语法应该被使用。

> **注意**:
>
> 如果无法形成有效的变量名，美元符号会保持原样。
>
> ``` php
> <?php
> echo "No interpolation $  has happened\n";
> echo "No interpolation $\n has happened\n";
> echo "No interpolation $2 has happened\n";
> ?>
> ```
>
> 以上示例会输出：
>
>     No interpolation $  has happened
>     No interpolation $
>      has happened
>     No interpolation $2 has happened

**示例 \#17 插值数组或属性的第一个维度值**

``` php
<?php
$juices = array("apple", "orange", "string_key" => "purple");

echo "He drank some $juices[0] juice.";
echo PHP_EOL;
echo "He drank some $juices[1] juice.";
echo PHP_EOL;
echo "He drank some $juices[string_key] juice.";
echo PHP_EOL;

class A {
    public $s = "string";
}

$o = new A();

echo "Object value: $o->s.";
?>
```

以上示例会输出：

    He drank some apple juice.
    He drank some orange juice.
    He drank some purple juice.
    Object value: string.

> **注意**:
>
> 数组键必须是无引号的，因此不能用基本语法将常量作为键来引用。使用 高级 语法代替。

从 PHP 7.1.0 起，还支持*负*数字索引。

**示例 \#18 负数索引**

``` php
<?php
$string = 'string';
echo "The character at index -2 is $string[-2].", PHP_EOL;
$string[-3] = 'o';
echo "Changing the character at index -3 to o gives $string.", PHP_EOL;
?>
```

以上示例会输出：

    The character at index -2 is n.
    Changing the character at index -3 to o gives strong.

对于更复杂的情况，可以使用 高级 语法。

##### 高级（大括号）语法

高级语法允许使用任意访问器对*变量*进行插值。

任何标量变量、数组元素或对象属性（static 或非 static）都可以通过这种语法进行插值。表达式的写法和 在string之外的写法一样，然后用大括号`{`和 `}`包围。由于`{`不能被转义，所以这种语法只有在 紧跟在`{`后面的`$`才会被识别。要得到一个字面的 `{$`，需要用`{\$`。以下是一些例子：

**示例 \#19 Curly Syntax**

``` php
<?php
const DATA_KEY = 'const-key';
$great = 'fantastic';
$arr = [
    '1',
    '2',
    '3',
    [41, 42, 43],
    'key' => 'Indexed value',
    'const-key' => 'Key with minus sign',
    'foo' => ['foo1', 'foo2', 'foo3']
];

// 无效，输出 This is { fantastic}
echo "This is { $great}";

// 有效，输出 This is fantastic
echo "This is {$great}";

class Square {
    public $width;

    public function __construct(int $width) { $this->width = $width; }
}

$square = new Square(5);

// 有效
echo "This square is {$square->width}00 centimeters wide.";


// 有效，引用 key 仅使用花括号语法时有效
echo "This works: {$arr['key']}";


// 有效
echo "This works: {$arr[3][2]}";

echo "This works: {$arr[DATA_KEY]}";

// 使用多维数组时，在字符串内部时，始终使用括号括住数组
echo "This works: {$arr['foo'][2]}";

echo "This works: {$obj->values[3]->name}";

echo "This works: {$obj->$staticProp}";

// 无效，输出 C:\directory\{fantastic}.txt
echo "C:\directory\{$great}.txt";

// 有效，输出 C:\directory\fantastic.txt
echo "C:\\directory\\{$great}.txt";
?>
```

> **注意**:
>
> 由于该语法允许任意表达式，因此可以在高级语法中使用 可变变量。

#### 存取和修改字符串中的字符

string 中的字符可以通过一个从 0 开始的下标，用类似 array 结构中的方括号包含对应的数字来访问和修改，比如 `$str[42]`。可以把 string 当成字符组成的 array。函数 substr() 和 substr_replace() 可用于操作多于一个字符的情况。

> **注意**:
>
> 从 PHP 7.1.0 开始，还支持 string 负偏移量。从 string 尾部到指定位置的偏移量。 以前，负偏移量读取时（返回空 string）会发出 **`E_NOTICE`**， 写入时（string 保持不变）会发出 **`E_WARNING`**。

> **注意**:
>
> PHP 8.0.0 之前, 出于同样的目的，可以使用大括号访问 string，例如 `$str{42}`。 从 PHP 7.4.0 起，此大括号语法被弃用，自 PHP 8.0.0 开始不再受支持。

**警告**

用超出字符串长度的下标写入将会拉长该字符串并以空格填充。非整数类型下标会被转换成整数。非法下标类型会产生一个 **`E_WARNING`** 级别错误。 写入时只用到了赋值字符串的第一个字符。 PHP 7.1.0 开始，用空字符串赋值会导致 fatal 错误；在之前赋给的值是 NULL 字符。

**警告**

PHP 的字符串在内部是字节组成的数组。因此用花括号访问或修改字符串对多字节字符集很不安全。仅应对单字节编码例如 ISO-8859-1 的字符串进行此类操作。

> **注意**:
>
> 从 PHP 7.1.0 开始，对空字符串应用空索引运算符会引发致命错误。 以前是空字符串会被静默转为数组。

**示例 \#20 一些字符串示例**

``` php
<?php
// 取得字符串的第一个字符
$str = 'This is a test.';
$first = $str[0];
var_dump($first);

// 取得字符串的第三个字符
$third = $str[2];
var_dump($third);

// 取得字符串的最后一个字符
$str = 'This is still a test.';
$last = $str[strlen($str)-1];
var_dump($last);

// 修改字符串的最后一个字符
$str = 'Look at the sea';
$str[strlen($str)-1] = 'e';
var_dump($str);
?>
```

字符串下标必须为整数或可转换为整数的字符串，否则会发出警告。之前类似 `"foo"` 的下标会无声地转换成 `0`。

**示例 \#21 字符串无效下标的例子**

``` php
<?php
$str = 'abc';

$keys = [ '1', '1.0', 'x', '1x' ];

foreach ($keys as $keyToTry) {
    var_dump(isset($str[$keyToTry]));

    try {
        var_dump($str[$keyToTry]);
    } catch (TypeError $e) {
        echo $e->getMessage(), PHP_EOL;
    }

    echo PHP_EOL;
}
?>
```

以上示例会输出：

    bool(true)
    string(1) "b"

    bool(false)
    Cannot access offset of type string on string

    bool(false)
    Cannot access offset of type string on string

    bool(false)

    Warning: Illegal string offset "1x" in Standard input code on line 10
    string(1) "b"

> **注意**:
>
> 用 `[]` 或 `{}` 访问任何其它类型（不包括数组或具有相应接口的对象实现）的变量只会无声地返回 **`null`**。

> **注意**:
>
> 可以直接在字符串原型中用 `[]` 或 `{}` 访问字符。

> **注意**:
>
> PHP 7.4 中弃用在字符串字面量中使用 `{}` 来访问字符。 PHP 8.0 已移除。

### 有用的函数和运算符

字符串可以用 '.'（点）运算符连接起来，注意 '+'（加号）运算符*没有*这个功能。更多信息参考字符串运算符。

对于 string 的操作有很多有用的函数。

可以参考字符串函数了解大部分函数，高级的查找与替换功能可以参考 Perl 兼容正则表达式函数。

另外还有 URL 字符串函数，也有加密／解密字符串的函数（Sodium 和 Hash）。

最后，可以参考字符类型函数。

### 转换成字符串

一个值可以通过在其前面加上 `(string)` 或用 strval() 函数来转变成字符串。在一个需要字符串的表达式中，会自动转换为 string。这发生在当使用 echo 或 print 函数，或当变量与 string 进行比较的时候。类型和类型转换可以更好的解释下面的事情，也可参考函数 settype()。

一个布尔值 bool 的 **`true`** 被转换成 string 的 `"1"`。bool 的 **`false`** 被转换成 `""`（空字符串）。这种转换可以在 bool 和 string 之间相互进行。

一个整数 int 或浮点数 float 被转换为数字的字面样式的 string（包括 float 中的指数部分）。使用指数计数法的浮点数（`4.1E+6`）也可转换。

> **注意**:
>
> PHP 8.0.0 起，十进制小数点字符都是一个句号（`.`）。 而在此之前的版本，在脚本的区域（category LC_NUMERIC） 中定义了十进制小数点字符。参见 setlocale()。

数组 array 总是转换成字符串 `"Array"`，因此，echo 和 print 无法显示出该数组的内容。要显示某个单元，可以用 `echo $arr['foo']` 这种结构。要显示整个数组内容见下文。

必须使用魔术方法 \_\_toString 才能将 object 转换为 string。

资源 Resource 总会被转变成 `"Resource id #1" ` 这种结构的字符串，其中的 `1` 是 PHP 在运行时分配给该 resource 的资源数字。 虽然不应依赖此字符串的确切结构且该结构可能会更改，但在脚本执行的生命周期内（即一个 Web 请求或 CLI 进程），该字符串对于给定的资源始终是唯一的，且不会被重复使用。 要得到一个 resource 的类型，可以用函数 get_resource_type()。

**`null`** 总是被转变成空字符串。

如上面所说的，直接把 array，object 或 resource 转换成 string 不会得到除了其类型之外的任何有用信息。可以使用函数 print_r() 和 var_dump() 列出这些类型的内容。

大部分的 PHP 值可以转变成 string 来永久保存，这被称作串行化，可以用函数 serialize() 来实现。

### 字符串类型详解

PHP 中的 string 的实现方式是一个由字节组成的数组再加上一个整数指明缓冲区长度。并无如何将字节转换成字符的信息，由程序员来决定。字符串由什么值来组成并无限制；特别的，其值为 `0`（“NUL bytes”）的字节可以处于字符串任何位置（不过有几个函数，在本手册中被称为非“二进制安全”的，也许会把 NUL 字节之后的数据全都忽略）。

字符串类型的此特性解释了为什么 PHP 中没有单独的“byte”类型 - 已经用字符串来代替了。返回非文本值的函数 - 例如从网络套接字读取的任意数据 - 仍会返回字符串。

由于 PHP 并不特别指明字符串的编码，那字符串到底是怎样编码的呢？例如字符串 `"á"` 到底是等于 `"\xE1"`（ISO-8859-1），`"\xC3\xA1"`（UTF-8，C form），`"\x61\xCC\x81"`（UTF-8，D form）还是任何其它可能的表达呢？答案是字符串会被按照该脚本文件相同的编码方式来编码。因此如果一个脚本的编码是 ISO-8859-1，则其中的字符串也会被编码为 ISO-8859-1，以此类推。不过这并不适用于激活了 Zend Multibyte 时；此时脚本可以是以任何方式编码的（明确指定或被自动检测）然后被转换为某种内部编码，然后字符串将被用此方式编码。注意脚本的编码有一些约束（如果激活了 Zend Multibyte 则是其内部编码）- 这意味着此编码应该是 ASCII 的兼容超集，例如 UTF-8 或 ISO-8859-1。不过要注意，依赖状态的编码其中相同的字节值可以用于首字母和非首字母而转换状态，这可能会造成问题。

当然了，要做到有用，操作文本的函数必须假定字符串是如何编码的。不幸的是，PHP 关于此的函数有很多变种：

- 某些函数假定字符串是以单字节编码的，但并不需要将字节解释为特定的字符。例如 substr()，strpos()，strlen() 和 strcmp()。理解这些函数的另一种方法是它们作用于内存缓冲区，即按照字节和字节下标操作。

- 某些函数被传递入了字符串的编码方式，也可能会假定默认无此信息。例如 htmlentities() 和 mbstring 扩展中的大部分函数。

- 其它函数使用了当前区域（见 setlocale()），但是逐字节操作。

- 最后一些函数会假定字符串是使用某特定编码的，通常是 UTF-8。intl 扩展和 PCRE（上例中仅在使用了 `u` 修饰符时）扩展中的大部分函数都是这样。

最后，要书写能够正确使用 Unicode 的程序依赖于很小心地避免那些可能会损坏数据的函数。要使用来自于 intl 和 mbstring 扩展的函数。不过使用能处理 Unicode 编码的函数只是个开始。不管用何种语言提供的函数，最基本的还是了解 Unicode 规格。例如一个程序如果假定只有大写和小写，那可是大错特错。

---

## [S2.8] Array

- url: https://www.php.net/manual/zh/language.types.array.php
- fidelity: verbatim
- fetched: 2026-11-22

## Array 数组

有关数组操作的更多信息，请参阅 数组函数 章节的文档。

PHP 中的 array 实际上是一个有序映射。映射是一种把 *values* 关联到 *keys* 的类型。此类型针对多种不同用途进行了优化； 它可以被视为数组、列表（向量）、哈希表（映射的实现）、字典、集合、堆栈、队列等等。 由于 array 的值可以是其它 array 所以树形结构和多维 array 也是允许的。

解释这些数据结构超出了本手册的范围，但对每种结构至少会提供一个例子。 要得到这些数据结构的更多信息，建议参考有关此广阔主题的其它文献。

### 语法

#### 定义数组 array()

可以用 array() 语言结构来新建一个 array。它接受任意数量用逗号分隔的 `键（key）`` => ``值（value）` 对。

``` synopsis
array(
    key  => value,
    key2 => value2,
    key3 => value3,
    ...
)
```

最后一个数组单元之后的逗号可以省略。通常用于单行数组定义中，例如常用 `array(1, 2)` 而不是 `array(1, 2, )`。对多行数组定义通常保留最后一个逗号，这样要添加一个新单元时更方便。

> **注意**:
>
> 可以用短数组语法 `[]` 替代 `array()` 。

**示例 \#1 一个简单数组**

``` php
<?php
$array1 = array(
    "foo" => "bar",
    "bar" => "foo",
);

// 使用短数组语法
$array2 = [
    "foo" => "bar",
    "bar" => "foo",
];

var_dump($array1, $array2);
?>
```

key 可以是 integer 或者 string。value 可以是任意类型。

此外 key 会有如下的强制转换：

- String 中包含有效的十进制 int，除非数字前面有一个 `+` 号，否则将被转换为 int 类型。例如键名 `"8"` 实际会被储存为 `8`。另外， `"08"` 不会被强制转换，因为它不是一个有效的十进制整数。

- Float 也会被转换为 int ，意味着其小数部分会被舍去。例如键名 `8.7` 实际会被储存为 `8`。

- Bool 也会被转换成 int。即键名 **`true`** 实际会被储存为 `1` 而键名 **`false`** 会被储存为 `0`。

- Null 会被转换为空字符串，即键名 `null` 实际会被储存为 `""`。

- Array 和 object *不能* 被用为键名。坚持这么做会导致警告：`Illegal offset type`。

如果在数组定义时多个元素都使用相同键名，那么只有最后一个会被使用，其它的元素都会被覆盖。

**示例 \#2 类型转换与覆盖的示例**

``` php
<?php
$array = array(
    1    => "a",
    "1"  => "b",
    1.5  => "c",
    true => "d",
);
var_dump($array);
?>
```

以上示例会输出：

    array(1) {
      [1]=>
      string(1) "d"
    }

上例中所有的键名都被强制转换为 `1`，则每一个新单元都会覆盖前一个的值，最后剩下的只有一个 `"d"`。

PHP 数组可以同时含有 int 和 string 类型的键名，因为 PHP 实际并不区分索引数组和关联数组。

**示例 \#3 混合 int 和 string 键名**

``` php
<?php
$array = array(
    "foo" => "bar",
    "bar" => "foo",
    100   => -100,
    -100  => 100,
);
var_dump($array);
?>
```

以上示例会输出：

    array(4) {
      ["foo"]=>
      string(3) "bar"
      ["bar"]=>
      string(3) "foo"
      [100]=>
      int(-100)
      [-100]=>
      int(100)
    }

key 为可选项。如果未指定，PHP 将自动使用之前用过的最大 int 键名加上 1 作为新的键名。

**示例 \#4 没有键名的索引数组**

``` php
<?php
$array = array("foo", "bar", "hello", "world");
var_dump($array);
?>
```

以上示例会输出：

    array(4) {
      [0]=>
      string(3) "foo"
      [1]=>
      string(3) "bar"
      [2]=>
      string(5) "hello"
      [3]=>
      string(5) "world"
    }

还可以只对某些单元指定键名而对其它的空置：

**示例 \#5 仅对部分单元指定键名**

``` php
<?php
$array = array(
         "a",
         "b",
    6 => "c",
         "d",
);
var_dump($array);
?>
```

以上示例会输出：

    array(4) {
      [0]=>
      string(1) "a"
      [1]=>
      string(1) "b"
      [6]=>
      string(1) "c"
      [7]=>
      string(1) "d"
    }

可以看到最后一个值 `"d"` 被自动赋予了键名 `7`。这是由于之前最大的整数键名是 `6`。

**示例 \#6 复杂类型转换和覆盖的例子**

这个例子包括键名类型转换和元素覆盖的所有变化。

``` php
<?php
$array = array(
    1    => 'a',
    '1'  => 'b', // 值 "a" 会被 "b" 覆盖
    1.5  => 'c', // 值 "b" 会被 "c" 覆盖
    -1 => 'd',
    '01'  => 'e', // 由于这不是整数字符串，因此不会覆盖键名 1
    '1.5' => 'f', // 由于这不是整数字符串，因此不会覆盖键名 1
    true => 'g', // 值 "c" 会被 "g" 覆盖
    false => 'h',
    '' => 'i',
    null => 'j', // 值 "i" 会被 "j" 覆盖
    'k', // 值 “k” 的键名被分配为 2。这是因为之前最大的整数键是 1
    2 => 'l', // 值 "k" 会被 "l" 覆盖
);

var_dump($array);
?>
```

以上示例会输出：

    array(7) {
      [1]=>
      string(1) "g"
      [-1]=>
      string(1) "d"
      ["01"]=>
      string(1) "e"
      ["1.5"]=>
      string(1) "f"
      [0]=>
      string(1) "h"
      [""]=>
      string(1) "j"
      [2]=>
      string(1) "l"
    }

**示例 \#7 负数索引示例**

当分配负整数 key `n` 时，PHP 会将下一个 key 分配给 `n+1`。

``` php
<?php
$array = [];

$array[-5] = 1;
$array[] = 2;

var_dump($array);
?>
```

以上示例会输出：

    array(2) {
      [-5]=>
      int(1)
      [-4]=>
      int(2)
    }

**警告**

PHP 8.3.0 之前，分配负整数 key `n` 会将下一个 key 分配给 `0`，因此前面的示例将输出：

    array(2) {
      [-5]=>
      int(1)
      [0]=>
      int(2)
    }

#### 用方括号语法访问数组单元

数组单元可以通过 `array[key]` 语法来访问。

**示例 \#8 访问数组单元**

``` php
<?php
$array = array(
    "foo" => "bar",
    42    => 24,
    "multi" => array(
         "dimensional" => array(
             "array" => "foo"
         )
    )
);

var_dump($array["foo"]);
var_dump($array[42]);
var_dump($array["multi"]["dimensional"]["array"]);
?>
```

以上示例会输出：

    string(3) "bar"
    int(24)
    string(3) "foo"

> **注意**:
>
> 在 PHP 8.0.0 之前，方括号和花括号可以互换使用来访问数组单元（例如 `$array[42]` 和 `$array{42}` 在上例中效果相同）。 花括号语法在 PHP 7.4.0 中已弃用，在 PHP 8.0.0 中不再支持。

**示例 \#9 数组解引用**

``` php
<?php
function getArray() {
    return array(1, 2, 3);
}

$secondElement = getArray()[1];

var_dump($secondElement);
?>
```

> **注意**:
>
> 试图访问一个未定义的数组键名与访问任何未定义变量一样：会导致 **`E_WARNING`** 级别错误信息（在 PHP 8.0.0 之前是 **`E_NOTICE`** 级别），其结果为 **`null`**。

> **注意**:
>
> 数组解引用非 string 的标量值会产生 **`null`**。 在 PHP 7.4.0 之前，它不会发出错误消息。 从 PHP 7.4.0 开始，这个问题产生 **`E_NOTICE`** ； 从 PHP 8.0.0 开始，这个问题产生 **`E_WARNING`** 。

#### 用方括号的语法新建／修改

可以通过明示地设定其中的值来修改现有的 array 。

这是通过在方括号内指定键名来给 array 赋值实现的。也可以省略键名，在这种情况下给变量名加上一对空的方括号（`[]`）。

``` synopsis
$arr[key] = value;
$arr[] = value;
// key 可以是 int 或 string
// value 可以是任意类型的值
```

如果 `$arr` 不存在或者设置为 **`null`** 或者 **`false`**，将会新建它，这也是另一种创建 array 的方法。不过并不鼓励这样做，因为如果 `$arr` 已经包含有值（例如来自请求变量的 string）则此值会保留而 `[]` 实际上代表着字符串访问运算符。初始化变量的最好方式是直接给其赋值。

> **注意**:
>
> 从 PHP 7.1.0 起，对字符串应用空索引操作符会抛出致命错误。以前，字符串被静默地转换为数组。

> **注意**:
>
> 从 PHP 8.1.0 起，弃用从 **`false`** 值中创建一个新数组。 但仍然允许从 **`null`** 或者未定义的变量中创建新数组。

要修改某个值，通过其键名给该单元赋一个新值。要删除某键值对，对其调用 unset() 函数。

**示例 \#10 Using Square Brackets with Arrays**

``` php
<?php
$arr = array(5 => 1, 12 => 2);

$arr[] = 56;    // 这与 $arr[13] = 56 相同;
                // 在脚本的这一点上

$arr["x"] = 42; // 添加一个新元素
                // 键名使用 "x"

unset($arr[5]); // 从数组中删除元素

unset($arr);    // 删除整个数组
?>
```

> **注意**:
>
> 如上所述，如果给出方括号但没有指定键名，则取当前最大 int 索引值，新的键名将是该值加上 1（但是最小为 0）。如果当前还没有 int 索引，则键名将为 `0` 。
>
> 注意这里所使用的最大整数键名*目前不需要存在于 array 中*。 它只要在上次 array 重新生成索引后曾经存在于 array 就行了。以下面的例子来说明：
>
> ``` php
> <?php
> // 创建一个简单的数组
> $array = array(1, 2, 3, 4, 5);
> print_r($array);
>
> // 现在删除其中的所有元素，但保持数组本身不变:
> foreach ($array as $i => $value) {
>     unset($array[$i]);
> }
> print_r($array);
>
> // 添加一个单元（注意新的键名是 5，而不是你可能以为的 0）
> $array[] = 6;
> print_r($array);
>
> // 重新索引：
> $array = array_values($array);
> $array[] = 7;
> print_r($array);
> ?>
> ```
>
> 以上示例会输出：
>
>     Array
>     (
>         [0] => 1
>         [1] => 2
>         [2] => 3
>         [3] => 4
>         [4] => 5
>     )
>     Array
>     (
>     )
>     Array
>     (
>         [5] => 6
>     )
>     Array
>     (
>         [0] => 6
>         [1] => 7
>     )

#### 数组解包

可以使用 `[]`（自 PHP 7.1.0 起）或者 list() 语言结构解包数组。这些结构可用于将数组解包为不同的变量。

**示例 \#11 Array Destructuring**

``` php
<?php
$source_array = ['foo', 'bar', 'baz'];

[$foo, $bar, $baz] = $source_array;

echo $foo, PHP_EOL;    // 打印 "foo"
echo $bar, PHP_EOL;    // 打印 "bar"
echo $baz, PHP_EOL;    // 打印 "baz"
?>
```

数组解包可用于 `foreach` 在迭代多维数组时对其进行解包。

**示例 \#12 Array Destructuring in Foreach**

``` php
<?php
$source_array = [
    [1, 'John'],
    [2, 'Jane'],
];

foreach ($source_array as [$id, $name]) {
    echo "{$id}: '{$name}'\n";
}
?>
```

如果变量未提供，数组元素将会被忽略。数组解包始终从索引 `0` 开始。

**示例 \#13 Ignoring Elements**

``` php
<?php
$source_array = ['foo', 'bar', 'baz'];

// 将索引 2 的元素分配给变量 $baz
[, , $baz] = $source_array;

echo $baz;    // 打印 "baz"
?>
```

自 PHP 7.1.0 起，也可以解包关联数组。这在数字索引数组中更容易选择正确的元素，因为可以显式指定索引。

**示例 \#14 Destructuring Associative Arrays**

``` php
<?php
$source_array = ['foo' => 1, 'bar' => 2, 'baz' => 3];

// 将索引 'baz' 处的元素分配给变量 $three
['baz' => $three] = $source_array;

echo $three, PHP_EOL;    // 打印 3

$source_array = ['foo', 'bar', 'baz'];

// 将索引 2 处的元素分配给变量 $baz
[2 => $baz] = $source_array;

echo $baz, PHP_EOL;    // 打印 "baz"
?>
```

数组解包可以方便的用于两个变量交换。

**示例 \#15 Swapping Two Variable**

``` php
<?php
$a = 1;
$b = 2;

[$b, $a] = [$a, $b];

echo $a, PHP_EOL;    // 打印 2
echo $b, PHP_EOL;    // 打印 1
?>
```

> **注意**:
>
> 分配时不支持展开运算符（`...`）。

> **注意**:
>
> 尝试访问未定义的数组键与访问任何未定义的变量相同：都将发出 **`E_WARNING`** 级别的错误消息（PHP 8.0.0 之前是 **`E_NOTICE`** 级别），结果将是 **`null`**。

> **注意**:
>
> 解构标量值会分配 **`null`** 到所有变量。

### 实用函数

有很多操作数组的函数，参见 数组函数 一节。

> **注意**:
>
> unset() 函数允许删除 array 中的某个键。但要注意数组将*不会*重建索引。如果需要删除后重建索引，可以用 array_values() 函数重建 array 索引。
>
> **示例 \#16 Unsetting Intermediate Elements**
>
> ``` php
> <?php
> $a = array(1 => 'one', 2 => 'two', 3 => 'three');
>
> /* 该数组将被定义为
>    $a = array(1 => 'one', 3 => 'three');
>    而不是
>    $a = array(1 => 'one', 2 =>'three');
> */
> unset($a[2]);
> var_dump($a);
>
> $b = array_values($a);
> // Now $b is array(0 => 'one', 1 =>'three')
> var_dump($b);
> ?>
> ```

`foreach` 控制结构是专门用于 array 的。它提供了一个简单的方法来遍历 array。

### 数组做什么和不做什么

#### 为什么 `$foo[bar]` 错了？

应该始终在用字符串表示的数组索引上加上引号。例如用 `$foo['bar']` 而不是 `$foo[bar]`。但是为什么呢？可能在老的脚本中见过如下语法：

``` php
<?php
$foo[bar] = 'enemy';
echo $foo[bar];
// 及其它
?>
```

这样是错的，但可以正常运行。那么为什么错了呢？原因是此代码中有一个未定义的常量（ `bar` ）而不是 string（`'bar'`－注意引号）。而 PHP 可能会在以后定义此常量，不幸的是你的代码中有同样的名字。它能运行，是因为 PHP 自动将*裸字符串*（没有引号的 string 且不对应于任何已知符号）转换成一个其值为该裸 string 的 string。例如，如果没有常量定义为 **`bar`**，那么PHP 将在 string 中替代为 `'bar'` 并使用之。

**警告**

将未定义的常量当作裸字符串的回退会触发 **`E_NOTICE`** 级别错误。 从 PHP 7.2.0 起已废弃，并触发 **`E_WARNING`** 级别错误。 从 PHP 8.0.0 起被移除，并触发 Error 异常。

这并不意味着*总是*给键名加上引号。用不着给键名为 常量 或 变量 的加上引号，否则会使 PHP 不能解析它们。

**示例 \#17 Key Quoting**

``` php
<?php
error_reporting(E_ALL);
ini_set('display_errors', true);
ini_set('html_errors', false);

// 简单数组:
$array = array(1, 2);
$count = count($array);

for ($i = 0; $i < $count; $i++) {
    echo "\n检查 $i: \n";
    echo "坏的: " . $array['$i'] . "\n";
    echo "好的: " . $array[$i] . "\n";
    echo "坏的: {$array['$i']}\n";
    echo "好的: {$array[$i]}\n";
}
?>
```

以上示例会输出：

    检查 0:
    Notice: Undefined index:  $i in /path/to/script.html on line 9
    坏的:
    好的: 1
    Notice: Undefined index:  $i in /path/to/script.html on line 11
    坏的:
    好的: 1

    检查 1:
    Notice: Undefined index:  $i in /path/to/script.html on line 9
    坏的:
    好的: 2
    Notice: Undefined index:  $i in /path/to/script.html on line 11
    坏的:
    好的: 2

演示此行为的更多例子：

**示例 \#18 More Examples**

``` php
<?php
// 显示所有错误
error_reporting(E_ALL);

$arr = array('fruit' => 'apple', 'veggie' => 'carrot');

// 正确
echo $arr['fruit'], PHP_EOL;  // apple
echo $arr['veggie'], PHP_EOL; // carrot

// 不正确。此操作无效，并会因未定义名为 fruit 的常量而抛出 PHP 错误
//
// Error: Undefined constant "fruit"
try {
    echo $arr[fruit];
} catch (Error $e) {
    echo get_class($e), ': ', $e->getMessage(), PHP_EOL;
}

// 此处定义了一个常量以说明其行为，将值 'veggie' 赋予名为 fruit 的常量
define('fruit', 'veggie');

// 注意现在不同
echo $arr['fruit'], PHP_EOL;  // apple
echo $arr[fruit], PHP_EOL;    // carrot

// 以下写法是允许的，因为其位于字符串内部。常量在字符串中不会被查找，因此此处不会产生错误
echo "Hello $arr[fruit]", PHP_EOL;      // Hello apple

// 例外：字符串中用花括号包围的数组允许对常量进行解析
echo "Hello {$arr[fruit]}", PHP_EOL;    // Hello carrot
echo "Hello {$arr['fruit']}", PHP_EOL;  // Hello apple

// 拼接是另一种选择
echo "Hello " . $arr['fruit'], PHP_EOL; // Hello apple
?>
```

``` php
// 这将不起作用，并会导致解析错误，例如：
// Parse error: parse error, expecting T_STRING' or T_VARIABLE' or T_NUM_STRING'
// 这当然也适用于在字符串中使用超全局变量
print "Hello $arr['fruit']";
print "Hello $_GET['foo']";
?>
```

和在 语法 一节中规定的一样，在方括号（`[`” 和 “`]`”）之间必须有一个表达式。这意味着可以这样写：

``` php
<?php
echo $arr[somefunc($bar)];
?>
```

这是一个用函数返回值作为数组索引的例子。PHP 也可以用已知常量，可能之前已经见过：

``` php
<?php
$error_descriptions[E_ERROR]   = "A fatal error has occurred";
$error_descriptions[E_WARNING] = "PHP issued a warning";
$error_descriptions[E_NOTICE]  = "This is just an informal notice";
?>
```

注意 `E_ERROR` 也是个合法的标识符，就和第一个例子中的 `bar` 一样。但是上一个例子实际上和如下写法是一样的：

``` php
<?php
$error_descriptions[1] = "A fatal error has occurred";
$error_descriptions[2] = "PHP issued a warning";
$error_descriptions[8] = "This is just an informal notice";
?>
```

因为 `E_ERROR` 等于 `1`，等等。

##### 那么为什么这样做不好？

也许有一天，PHP 开发小组可能会想新增一个常量或者关键字，或者用户可能希望以后在自己的程序中引入新的常量，那就有麻烦了。例如已经不能这样用 `empty` 和 `default` 这两个词了，因为他们是 保留关键字。

> **注意**:
>
> 重申一次，在双引号字符串中，不给索引加上引号是合法的因此 `"$foo[bar]"` 是合法的（“合法”的原文为 valid。在实际测试中，这么做确实可以访问数组的该元素，但是会报一个常量未定义的 notice。无论如何，强烈建议不要使用 \$foo\[bar\]这样的写法，而要使用 \$foo\['bar'\] 来访问数组中元素。--haohappy 注）。至于为什么参见以上的例子和 字符串中的变量解析 中的解释。

### 转换为数组

对于任意 int，float， string，bool 和 resource 类型，如果将一个值转换为 array，将得到一个仅有一个元素的数组，其下标为 0，该元素即为此标量的值。换句话说，`(array) $scalarValue` 与 `array($scalarValue)` 完全一样。

如果将 object 类型转换为 array，则结果为一个数组，其单元为该对象的属性。键名将为成员变量名，不过有几点例外：整数属性不可访问； 私有变量前会加上类名作前缀；保护变量前会加上一个 '\*' 做前缀。这些前缀的前后都各有一个 `NUL` 字节。 未初始化的类型属性将会被丢弃。

**示例 \#19 转换为数组**

``` php
<?php

class A {
    private $B;
    protected $C;
    public $D;
    function __construct()
    {
        $this->{1} = null;
    }
}

var_export((array) new A());
?>
```

以上示例会输出：

    array (
      '' . "\0" . 'A' . "\0" . 'B' => NULL,
      '' . "\0" . '*' . "\0" . 'C' => NULL,
      'D' => NULL,
      1 => NULL,
    )

这些 `NUL` 会导致一些意想不到的行为：

**示例 \#20 Casting an Object to an Array**

``` php
<?php

class A {
    private $A; // 将变为 '\0A\0A'
}

class B extends A {
    private $A; // 将变为 '\0B\0A'
    public $AA; // 将变为 'AA'
}

var_dump((array) new B());
?>
```

以上示例会输出：

    array(3) {
      ["BA"]=>
      NULL
      ["AA"]=>
      NULL
      ["AA"]=>
      NULL
    }

上例会有两个键名为 'AA'，不过其中一个实际上是 '\0A\0A'。

将 **`null`** 转换为 array 会得到一个空的数组。

### 比较

可以用 array_diff() 函数和数组运算符来比较数组。

### 数组解包

在 array 定义时，用 `...` 前缀的一个 array 可以被展开到当前位置。 只有实现了 Traversable 的数组和对象才能被展开。 PHP 7.4.0 开始可以使用 `...` 解包 array。这也被称之为展开运算符。

它可以多次使用，在 `...` 操作符前后都可以添加常规元素：

**示例 \#21 简单的数组解包**

``` php
<?php
// 使用简短的数组语法。
// 亦可用于 array() 语法
$arr1 = [1, 2, 3];
$arr2 = [...$arr1]; // [1, 2, 3]
$arr3 = [0, ...$arr1]; // [0, 1, 2, 3]
$arr4 = [...$arr1, ...$arr2, 111]; // [1, 2, 3, 1, 2, 3, 111]
$arr5 = [...$arr1, ...$arr1]; // [1, 2, 3, 1, 2, 3]

function getArr() {
  return ['a', 'b'];
}
$arr6 = [...getArr(), 'c' => 'd']; // ['a', 'b', 'c' => 'd']

var_dump($arr1, $arr2, $arr3, $arr4, $arr5, $arr6);
?>
```

`...` 操作符解包 array 时也遵守函数 array_merge() 的语义。 也就是说，key 为字符时，后面的字符键会覆盖之前的字符键；key 为 integer 时则会重新编号：

**示例 \#22 重复 key 的数组解包**

``` php
<?php
// string key
$arr1 = ["a" => 1];
$arr2 = ["a" => 2];
$arr3 = ["a" => 0, ...$arr1, ...$arr2];
var_dump($arr3); // ["a" => 2]

// integer key
$arr4 = [1, 2, 3];
$arr5 = [4, 5, 6];
$arr6 = [...$arr4, ...$arr5];
var_dump($arr6); // [1, 2, 3, 4, 5, 6]
// 即 [0 => 1, 1 => 2, 2 => 3, 3 => 4, 4 => 5, 5 => 6]
// 也就是原始的 integer key 不再保留
?>
```

> **注意**:
>
> 既不是 integer 也不是 string 的 key 会抛出 TypeError。 这类 key 只能通过 Traversable 对象生成。

> **注意**:
>
> 在 PHP 8.1 之前，带有 string 键的 array 无法解包：
>
> ``` php
> <?php
>
> $arr1 = [1, 2, 3];
> $arr2 = ['a' => 4];
> $arr3 = [...$arr1, ...$arr2];
> // Fatal error: Uncaught Error: Cannot unpack array with string keys in example.php:5
>
> $arr4 = [1, 2, 3];
> $arr5 = [4, 5];
> $arr6 = [...$arr4, ...$arr5]; // works. [1, 2, 3, 4, 5]
> ?>
> ```

### 示例

PHP 中的数组类型有非常多的用途。以下是一些示例：

**示例 \#23 Array Versatility**

``` php
<?php
// 这里：
$a = array( 'color' => 'red',
            'taste' => 'sweet',
            'shape' => 'round',
            'name'  => 'apple',
            4        // 键名为 0
          );

$b = array('a', 'b', 'c');

var_dump($a, $b);

// . . .完全等同于:
$a = array();
$a['color'] = 'red';
$a['taste'] = 'sweet';
$a['shape'] = 'round';
$a['name']  = 'apple';
$a[]        = 4;        // 键名为 0

$b = array();
$b[] = 'a';
$b[] = 'b';
$b[] = 'c';

// 执行上述代码后，数组 $a 将是
// array('color' => 'red', 'taste' => 'sweet', 'shape' => 'round',
// 'name' => 'apple', 0 => 4)， 数组 $b 将是
// array(0 => 'a', 1 => 'b', 2 => 'c'), 或简单的 array('a', 'b', 'c').
?>
```

**示例 \#24 使用 array()**

``` php
<?php
// Array as (property-)map
$map = array( 'version'    => 4,
              'OS'         => 'Linux',
              'lang'       => 'english',
              'short_tags' => true
            );
var_dump($map);

// strictly numerical keys
// this is the same as array(0 => 7, 1 => 8, ...)
$array = array( 7,
                8,
                0,
                156,
                -10
              );
var_dump($array);

$switching = array(         10, // key = 0
                    5    =>  6,
                    3    =>  7,
                    'a'  =>  4,
                            11, // key = 6 (整数索引的最大值为 5)
                    '8'  =>  2, // key = 8 (整数！)
                    '02' => 77, // key = '02'
                    0    => 12  // 值 10 被 12 覆盖
                  );
var_dump($switching);

// 空数组
$empty = array();
var_dump($empty);
?>
```

**示例 \#25 集合**

``` php
<?php
$colors = array('red', 'blue', 'green', 'yellow');

foreach ($colors as $color) {
    echo "Do you like $color?\n";
}

?>
```

以上示例会输出：

    Do you like red?
    Do you like blue?
    Do you like green?
    Do you like yellow?

可以通过引用传递 array 的值来直接更改数组的值。

**示例 \#26 在循环中改变单元**

``` php
<?php
$colors = array('red', 'blue', 'green', 'yellow');

foreach ($colors as &$color) {
    $color = mb_strtoupper($color);
}
unset($color); /* 确保后面对
$color 的写入不会修改最后一个数组元素 */

print_r($colors);
?>
```

以上示例会输出：

    Array
    (
        [0] => RED
        [1] => BLUE
        [2] => GREEN
        [3] => YELLOW
    )

本例生成一个下标从 1 开始的数组。

**示例 \#27 下标从 1 开始的数组**

``` php
<?php
$firstquarter = array(1 => 'January', 'February', 'March');
print_r($firstquarter);
?>
```

以上示例会输出：

    Array
    (
        [1] => January
        [2] => February
        [3] => March
    )

**示例 \#28 填充数组**

``` php
<?php
// 把指定目录中的所有项填充到数组
$handle = opendir('.');
while (false !== ($file = readdir($handle))) {
    $files[] = $file;
}
closedir($handle);

var_dump($files);
?>
```

Array 是有序的。也可以使用不同的排序函数来改变顺序。更多信息参见 数组函数。可以用 count() 函数来统计出 array 中元素的个数。

**示例 \#29 数组排序**

``` php
<?php
sort($files);
print_r($files);
?>
```

因为 array 中的值可以为任意值，也可是另一个 array。这样可以产生递归或多维 array。

**示例 \#30 递归和多维数组**

``` php
<?php
$fruits = array ( "fruits"  => array ( "a" => "orange",
                                       "b" => "banana",
                                       "c" => "apple"
                                     ),
                  "numbers" => array ( 1,
                                       2,
                                       3,
                                       4,
                                       5,
                                       6
                                     ),
                  "holes"   => array (      "first",
                                       5 => "second",
                                            "third"
                                     )
                );
var_dump($fruits);

// 处理上面数组中的值的一些例子
echo $fruits["holes"][5];    // 打印 "second"
echo $fruits["fruits"]["a"]; // 打印 "orange"
unset($fruits["holes"][0]);  // 删除 "first"

// 创建一个新的多维数组
$juices["apple"]["green"] = "good";
var_dump($juices);
?>
```

Array 的赋值总是会涉及到值的拷贝。使用 引用运算符 通过引用来拷贝 array。

**示例 \#31 Array Copying**

``` php
<?php
$arr1 = array(2, 3);
$arr2 = $arr1;
$arr2[] = 4; // $arr2 已更改，
             // $arr1 仍然是 array(2, 3)

$arr3 = &$arr1;
$arr3[] = 4; // 现在 $arr1 和 $arr3 是一样的

var_dump($arr1, $arr2, $arr3);
?>
```

---

## [S2.9] 型別轉換

- url: https://www.php.net/manual/zh/language.types.type-juggling.php
- fidelity: verbatim
- fetched: 2026-11-22

## 类型转换

PHP 在变量声明时不需要定义类型。在这种情况下，变量的类型由存储的值决定。也就是说，如果 string 赋值给 `$var`，然后 `$var` 的类型就是 string。之后将 int 值赋值给 `$var`，它将是 int 类型。

PHP 可能会尝试在某些上下文中自动将值转换为另一种类型。不同的上下文有：

- 数字

- 字符串

- 逻辑

- 整数和字符串

- 比较

- 函数

> **注意**:
>
> 当值需要解释为不同类型时，值本身*不*会改变类型。

强制将变量当做某种变量来求值，参见类型转换一节。要更改变量的类型，请参阅 settype() 函数。

### 数字上下文

使用算术运算符时的上下文。

在这种情况下，如果任一运算对象是 float（或者不能解释为 int），则两个运算对象都将解释为 float，结果也将是 float。否则，运算对象将解释为 int，结果也将是 int。自 PHP 8.0.0 起，如果无法解释其中一个运算对象，则会抛出 TypeError。

### 字符串上下文

使用 echo、print、字符串插值或者字符串连接运算符时的上下文。

这种情况下，值将会解释为 string。如果值无法解释，那么会抛出 TypeError。在 PHP 7.4.0 之前，会引发 **`E_RECOVERABLE_ERROR`**。

### 逻辑上下文

使用条件语句、三元运算符或逻辑运算符时的上下文。

在这种情况下，值将会解释为 bool。

### 整数和字符串上下文

使用位运算符时的上下文。

在这种情况下，如果所有的运算对象都是 string，则结果也将是 string。否则运算对象将解释为 int，结果也将是 int。如果其中一个运算对象无法解释，则会抛出 TypeError。

### 比较上下文

使用比较运算符时的上下文。

在此上下文中发生的类型转换在比较多种类型表中进行了说明。

### 函数上下文

将值传递给已声明类型的参数、属性，或从声明了返回类型的函数返回值时的上下文。

在此上下文中，值必须是类型值。但存在两个例外，第一个是如果值为 int，但声明的类型是 float，然后整数会转换为浮点数。第二个是如果声明的类型是 *scalar* 类型，值可转换为标量类型，并且强制类型模式处于活动状态（默认），值会转换为可接受的标量值。参见下文查看有关此行为的描述。

**警告**

内部函数自动将 **`null`** 转换为标量类型，此行为自 PHP 8.1.0 起*弃用*。

#### 使用简单类型声明的强制类型

- bool 类型声明：值将解释为 bool。

- int 类型声明：如果明确定义转换，则值将解释为 int。例如，字符串是数字。

- float 类型声明：如果明确定义转换，则值将解释为 float。例如，字符串是数字。

- string 类型声明：值将解释为 string。

#### 使用联合类型的强制类型

当未启用 `strict_types` 时，声明的标量类型会受到有限的隐式类型转换的影响。如果值的精确类型不是联合的一部分，然后会按照以下优先顺序选择目标类型：

1.  int

2.  float

3.  string

4.  bool

如果类型存在于 union 类型中，并且值可以根据 PHP 现有的类型检查语义转换为此类型，则选择该类型。否则，尝试下一个类型

**警告**

有个例外，如果值是字符串，并且 int 和 float 都是联合类型的一部分，首选类型则通过现有的数字字符串语义决定。例如 `"42"` 选择 int，`"42.0"` 选择 float。

> **注意**:
>
> 不属于上述优先级列表的类型不会进行隐式转换。特别是，不会出现对 null、false 和 true 类型的隐式转换。

**示例 \#1 类型转换为 union 类型中的一个的示例**

``` php
<?php
// int|string
42    --> 42          // 具体类型
"42"  --> "42"        // 具体类型
new ObjectWithToString --> "Result of __toString()"
                      // 对象绝不会兼容 int，回退到 string
42.0  --> 42          // int 兼容 float
42.1  --> 42          // int 兼容 float
1e100 --> "1.0E+100"  // float 对于 int 类型来说太大了，回退为 string
INF   --> "INF"       // float 对于 int 类型来说太大了，回退为 string
true  --> 1           // int 兼容 bool
[]    --> TypeError   // int 或 string 不兼容 array

// int|float|bool
"45"    --> 45        // int 数字 string
"45.0"  --> 45.0      // float 数字 string

"45X"   --> true      // 不是 numeric string，回退为 bool
""      --> false     // 不是 numeric string，回退为 bool
"X"     --> true      // 不是 numeric string，回退为 bool
[]      --> TypeError // int、float 或 bool 不兼容 array
?>
```

### 类型转换

类型转换通过在值前面的括号中写入类型来将值转换指定的类型。

**示例 \#2 类型转换**

``` php
<?php
$foo = 10;   // $foo 是 int
$bar = (bool) $foo;   // $bar 是 bool

var_dump($bar);
?>
```

允许的转换是：

- `(int)` ——转换为 int
- `(bool)` ——转换为 bool
- `(float)` ——转换为 float
- `(string)` ——转换为 string
- `(array)` ——转换为 array
- `(object)` ——转换为 object
- `(unset)` ——转换为 NULL

**警告**

`(integer)` 是 `(int)` 转换的别名。`(boolean)` 是 `(bool)` 转换的别名。`(binary)` 是 `(string)` 转换的别名。`(double)` 和 `(real)` 是 `(float)` 转换的别名。这些转换不使用标准的类型名称，自 PHP 8.5.0 起已弃用。

**警告**

自 PHP 7.4.0 起弃用 `(real)` 转换别名，并在 PHP 8.0.0 中移除。

**警告**

自 PHP 7.2.0 起弃用 `(unset)` 转换。注意 `(unset)` 转换等同于将值 NULL 通过赋值或者调用给变量。自 PHP 8.0.0 起移除 `unset` 转换。

**警告**

向前兼容 `(binary)` 转换和 `b` 前缀转换。注意 `(binary)` 转换和 `(string)` 相同，但是这可能会改变且不应依赖。

> **注意**:
>
> 类型转换的括号中的空格将被忽略。 因此，以下两个转换是等价的：
>
> ``` php
> <?php
> $foo = (int) $bar;
> $foo = ( int ) $bar;
> ?>
> ```

将文字 string 和变量转换为二进制 string：

``` php
<?php
$binary = (binary) $string;
$binary = b"binary string";
?>
```

除了将变量转换为 string 之外，还可以将变量放在双引号内。

**示例 \#3 不同的转换机制**

``` php
<?php
$foo = 10;            // $foo 是 int
$str = "$foo";        // $str 是 string
$fst = (string) $foo; // $fst 也是 string

// 打印出 "they are the same"
if ($fst === $str) {
    echo "they are the same", PHP_EOL;
}
?>
```

有时在类型之间转换时确切地会发生什么可能不是很明显。更多信息见如下不分：

- 转换为 bool
- 转换为 int
- 转换为 float
- 转换为 string
- 转换为 array
- 转换为 object
- 转换为 resource
- 转换为 NULL
- 类型比较表

> **注意**:
>
> 因为 PHP 的 string 支持使用与 array 索引相同的语法，通过偏移量进行索引，所以以下示例适用于所有 PHP 版本：
>
> **示例 \#4 使用字符串的数组偏移**
>
> ``` php
> <?php
> $a    = 'car'; // $a 是 string
> $a[0] = 'b';   // $a 依然是 string
> echo $a;       // bar
> ?>
> ```
>
> 请查看章节标题为存取和修改字符串中的字符获取更多信息。
