# S3 變數（raw）

- 章節：`language.variables`
- 取得方式：curl 下載 https://www.php.net/manual/zh/<頁面>.php 原始 HTML → 擷取 `div#<頁面ID>` 正文 → 排除 User Contributed Notes → pandoc 轉 Markdown（tools/fetch_raw.py）
- 抓取日期：2026-11-22
- 本檔為官方手冊原文（簡體中文），不可修改。

---

## [S3.1] 基礎

- url: https://www.php.net/manual/zh/language.variables.basics.php
- fidelity: verbatim
- fetched: 2026-11-22

## 基础

PHP 中的变量用一个美元符号后面跟变量名来表示。变量名是区分大小写的。

有效的变量名由字母（`A-Z`、`a-z` 或 128 到 255 之间的字节）或者下划线开头，后面跟上任意数量的字母，数字，或者下划线。 按照正常的正则表达式，它将被表述为：`^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`。

> **注意**:
>
> PHP 不支持 Unicode 变量名，但是，某些字符编码（例如 UTF-8）会以这样的方式对字符进行编码，即多字节字符的所有字节都在允许的范围内，从而使其成为有效的变量名。

> **注意**:
>
> `$this` 是一个特殊的变量，它不能被赋值。PHP 7.1.0 之前，间接赋值（例如通过使用可变变量）是可能的。

**小技巧**

请参见用户空间命名指南。

**示例 \#1 有效变量名**

``` php
<?php
$var = 'Bob';
$Var = 'Joe';
echo "$var, $Var";      // 输出 "Bob, Joe"

$_4site = 'not yet';    // 合法变量名；以下划线开头
$i站点is = 'mansikka';  // 合法变量名；可以用中文
?>
```

**示例 \#2 无效变量名**

``` php
<?php
$4site = 'not yet';     // 非法变量名；以数字开头
```

PHP 接受任意字节序列作为变量名。不遵循上述命名规则的变量名只能在运行时动态访问。有关如何访问变量的信息，请参阅可变变量。

**示例 \#3 访问模糊的变量名**

``` php
<?php
${'invalid-name'} = 'bar';
$name = 'invalid-name';
echo ${'invalid-name'}, " ", $$name;
?>
```

以上示例会输出：

    bar bar

变量默认始终传值赋值。那也就是说，当表达式的值赋值给变量时，整个原始表达式的值被赋值到目标变量。这意味着，例如，当一个变量的值赋予另外一个变量时，改变其中一个变量的值，将不会影响到另外一个变量。有关这种类型的赋值操作，请参阅表达式一章。

PHP 也提供了另外一种方式给变量赋值：引用赋值。这意味着新的变量简单的引用（换言之，“成为其别名” 或者 “指向”）了原始变量。改动新的变量将影响到原始变量，反之亦然。

使用引用赋值，简单地将一个 & 符号加到将要赋值的变量前（源变量）。例如，下列代码片断将输出“My name is Bob”两次：

``` php
<?php
$foo = 'Bob';              // 将 'Bob' 赋给 $foo
$bar = &$foo;              // 通过 $bar 引用 $foo
$bar = "My name is $bar";  // 修改 $bar 变量
echo $bar;
echo $foo;                 // $foo 的值也被修改
?>
```

有一点重要事项必须指出，那就是只有变量才可以引用赋值。

``` php
<?php
$foo = 25;
$bar = &$foo;      // 合法的赋值
$bar = &(24 * 7);  // 非法; 引用没有名字的表达式

function test()
{
   return 25;
}

$bar = &test();    // 无效，因为 test() 没有通过引用返回变量。
?>
```

在 PHP 中声明变量不是必需的，但这是一种非常好的做法。访问未定义的变量将导致 **`E_WARNING`**（在 PHP 8.0.0 之前，为 **`E_NOTICE`**）。未定义的变量的默认值为 **`null`**。isset() 语言结构可用于检测变量是否已初始化。

**示例 \#4 未初始化变量的默认值**

``` php
<?php
// 未设置和未引用（不使用上下文）的变量。
var_dump($unset_var);
?>
```

以上示例会输出：

    Warning: Undefined variable $unset_var in ...
    NULL

PHP 允许从未定义的变量自动生成数组（自动创建新数组）。 将元素追加到未定义的变量将创建一个新数组，并且不会生成警告。

**示例 \#5 未定义变量自动生成数组**

``` php
<?php
$unset_array[] = 'value'; // 不会生成警告。
?>
```

**警告**

当将一个文件包含在另一个使用相同变量名的文件中时，依赖未初始化变量的默认值是有问题的。

可以使用 unset() 语言结构来销毁变量。

有关变量相关函数的信息，请参阅变量函数参考。

---

## [S3.2] 作用域

- url: https://www.php.net/manual/zh/language.variables.scope.php
- fidelity: verbatim
- fetched: 2026-11-22

## 变量作用域

变量的作用域是定义该变量的上下文。PHP 有函数作用域和全局作用域。在函数之外定义的任何变量都仅限于全局作用域。当包含文件时，该文件中的代码继承了包含语句所在行的变量作用域。

**示例 \#1 全局变量作用域示例**

``` php
<?php
$a = 1;
include 'b.inc'; // 变量 $a 将在 b.inc 内可用
?>
```

在命名函数或匿名函数内创建的任何变量都仅限于函数主体的作用域。然而，箭头函数会绑定父级作用域中的变量，使其在函数体内可用。如果在函数内部 include 文件，那么包含文件中的变量将如同在调用函数内部定义一样可用。

**示例 \#2 局部变量作用域的示例**

``` php
<?php
$a = 1; // 全局作用域

function test()
{ 
    echo $a; // $a 变量 $a 未定义，因为它引用了 $a 的局部版本
}
?>
```

下面的示例会生成未定义变量 **`E_WARNING`**（PHP 8.0.0 之前是 **`E_NOTICE`**）诊断提示。这是因为 echo 语句引用了局部版本的变量 `$a`，而且在这个作用域内，它并没有被赋值。注意这与 C 语言有一点点不同，因为 C 中的全局变量会自动提供给函数，除非被局部定义特别覆盖。这可能引起一些问题，有些人可能不小心就改变了一个全局变量。PHP 中全局变量在函数中使用时必须声明为 global。

### `global` 关键字

`global` 关键字用于将变量从全局作用域绑定到局部作用域。该关键字可以与变量列表或单个变量一起使用。将创建引用同名全局变量的局部变量。如果全局变量不存在，则将在全局作用域内创建该变量并赋值为 **`null`**。

**示例 \#3 使用 `global`**

``` php
<?php
$a = 1;
$b = 2;

function Sum()
{
    global $a, $b;

    $b = $a + $b;
}

Sum();
echo $b;
?>
```

以上示例会输出：

    3

在函数中声明了全局变量 `$a` 和 `$b` 之后，对任一变量的所有引用都会指向其全局版本。对于一个函数能够声明的全局变量的最大个数，PHP 没有限制。

在全局作用域内访问变量的第二个办法，是用特殊的 PHP 自定义 `$GLOBALS` 数组。前面的例子可以写成：

**示例 \#4 使用 `$GLOBALS` 替代 global**

``` php
<?php
$a = 1;
$b = 2;

function Sum()
{
    $GLOBALS['b'] = $GLOBALS['a'] + $GLOBALS['b'];
}

Sum();
echo $b;
?>
```

`$GLOBALS` 是一个关联数组，每一个变量为一个元素，键名对应变量名，值对应变量的内容。`$GLOBALS` 之所以在全局作用域内存在，是因为 \$GLOBALS 是一个超全局变量。以下范例显示了超全局变量的用处：

**示例 \#5 演示超全局变量和作用域的例子**

``` php
<?php
function test_superglobal()
{
    echo $_POST['name'];
}
?>
```

> **注意**:
>
> 在函数外部使用 `global` 关键字不是错误。如果文件是从函数内部 include 的，则可以使用它。

### 使用 `static` 变量

变量作用域的另一个重要特性是 *static* 变量。静态变量仅在局部函数作用域中存在，但当程序执行离开此作用域时，其值并不丢失。看看下面的例子：

**示例 \#6 演示需要静态变量的例子**

``` php
<?php
function Test()
{
    $a = 0;
    echo $a;
    $a++;
}
?>
```

本函数没什么用处，因为每次调用时都会将 `$a` 的值设为 `0` 并输出 `0`。将变量加一的 `$a`++ 没有作用，因为一旦退出本函数则变量 `$a` 就不存在了。要写一个不会丢失本次计数值的计数函数，要将变量 `$a` 定义为静态的：

**示例 \#7 使用静态变量的例子**

``` php
<?php
function test()
{
    static $a = 0;
    echo $a;
    $a++;
}
?>
```

现在，变量 `$a` 仅在第一次调用 test() 函数时被初始化，之后每次调用 test() 函数都会输出 `$a` 的值并加一。

静态变量也提供了一种处理递归函数的方法。以下这个简单的函数递归计数到 10，使用静态变量 `$count` 来判断何时停止：

**示例 \#8 静态变量与递归函数**

``` php
<?php
function test()
{
    static $count = 0;

    $count++;
    echo $count;
    if ($count < 10) {
        test();
    }
    $count--;
}
?>
```

在 PHP 8.3.0 之前，静态变量只能使用常量表达式进行初始化。自 PHP 8.3.0 起，还允许使用动态表达式（例如函数调用）：

**示例 \#9 声明静态变量**

``` php
<?php
function foo(){
    static $int = 0;          // 正确
    static $int = 1+2;        // 正确
    static $int = sqrt(121);  // 自 PHP 8.3.0 起正确

    $int++;
    echo $int;
}
?>
```

匿名函数内的静态变量仅在该特定函数实例中存在。如果每次调用时都重新创建匿名函数，则静态变量将重新初始化。

**示例 \#10 匿名函数内的静态变量**

``` php
<?php
function exampleFunction($input) {
    $result = (static function () use ($input) {
        static $counter = 0;
        $counter++;
        return "Input: $input, Counter: $counter\n";
    });

    return $result();
}

// 调用 exampleFunction 将重新创建匿名函数，因此静态
// 变量不会保留其值。
echo exampleFunction('A'); // 输出：Input: A, Counter: 1
echo exampleFunction('B'); // 输出：Input: B, Counter: 1
?>
```

从 PHP 8.1.0 开始，当继承（不是覆盖）使用有静态变量的方法时，继承的方法将会跟父级方法共享静态变量。这意味着方法中的静态变量现在跟静态属性有相同的行为。

自 PHP 8.3.0 起，可以使用任意表达式初始化静态变量。这意味着也说，像是方法调用可用于初始化静态变量。

**示例 \#11 在继承方法中使用静态变量**

``` php
<?php
class Foo {
    public static function counter() {
        static $counter = 0;
        $counter++;
        return $counter;
    }
}
class Bar extends Foo {}
var_dump(Foo::counter()); // int(1)
var_dump(Foo::counter()); // int(2)
var_dump(Bar::counter()); // int(3)，PHP 8.1.0 之前 int(1)
var_dump(Bar::counter()); // int(4)，PHP 8.1.0 之前 int(2)
?>
```

### `global` 和 `static` 变量的引用

对于变量的 static 和 global 定义是以引用的方式实现的。例如，在一个函数作用域内部用 `global` 语句导入的一个真正的全局变量实际上是建立了一个到全局变量的引用。这有可能导致预料之外的行为，如以下例子所演示的：

``` php
<?php
function test_global_ref() {
    global $obj;
    $new = new stdClass;
    $obj = &$new;
}

function test_global_noref() {
    global $obj;
    $new = new stdClass;
    $obj = $new;
}

test_global_ref();
var_dump($obj);
test_global_noref();
var_dump($obj);
?>
```

以上示例会输出：

    NULL
    object(stdClass)#1 (0) {
    }

类似的行为也适用于 `static` 语句。引用并不是静态地存储的：

``` php
<?php
function &get_instance_ref() {
    static $obj;

    echo 'Static object: ';
    var_dump($obj);
    if (!isset($obj)) {
        $new = new stdClass;
        // 将一个引用赋值给静态变量
        $obj = &$new;
    }
    if (!isset($obj->property)) {
        $obj->property = 1;
    } else {
        $obj->property++;
    }
    return $obj;
}

function &get_instance_noref() {
    static $obj;

    echo 'Static object: ';
    var_dump($obj);
    if (!isset($obj)) {
        $new = new stdClass;
        // 将一个对象赋值给静态变量
        $obj = $new;
    }
    if (!isset($obj->property)) {
        $obj->property = 1;
    } else {
        $obj->property++;
    }
    return $obj;
}

$obj1 = get_instance_ref();
$still_obj1 = get_instance_ref();
echo "\n";
$obj2 = get_instance_noref();
$still_obj2 = get_instance_noref();
?>
```

以上示例会输出：

    Static object: NULL
    Static object: NULL

    Static object: NULL
    Static object: object(stdClass)#3 (1) {
      ["property"]=>
      int(1)
    }

此示例说明，当把引用赋值给静态变量时，第二次调用 `&get_instance_ref()` 函数时不会*记住*该引用。

---

## [S3.3] 可變變數

- url: https://www.php.net/manual/zh/language.variables.variable.php
- fidelity: verbatim
- fetched: 2026-11-22

## 可变变量

有时候使用可变变量名是很方便的。就是说，一个变量的变量名可以动态的设置和使用。一个普通的变量通过声明来设置，例如：

``` php
<?php
$a = 'hello';
?>
```

一个可变变量获取了一个普通变量的值作为这个可变变量的变量名。在上面的例子中 *hello* 使用了两个美元符号（\$）以后，就可以作为一个可变变量的变量了。例如：

``` php
<?php
$$a = 'world';
?>
```

这时，两个变量都被定义了：`$a` 的内容是“hello”并且 `$hello` 的内容是“world”。因此，以下语句：

``` php
<?php
echo "$a {$$a}";
?>
```

与以下语句输出完全相同的结果：

``` php
<?php
echo "$a $hello";
?>
```

它们都会输出：hello world。

要将可变变量用于数组，必须解决模棱两可的问题。也就是说，如果解析器看到 `$$a[1]`，那么解析器需要知道是将 `$a[1]` 作为变量，还是将 `$$a` 作为个变量并取出该变量中索引为 `[1]` 的值。解决此问题的语法是，对第一种情况用 `${$a[1]}`，对第二种情况用 `${$a}[1]`。

类的属性也可以通过可变属性名来访问。可变属性名将在该调用所处的作用域内被解析。例如，对于 `$foo->$bar` 表达式，则会在局部作用域来解析 `$bar` 并且其值将被用于 `$foo` 的属性名。对于 `$bar` 是数组单元时也是一样。

也可使用花括号来给属性名清晰定界。最有用是在属性位于数组中，或者属性名包含有多个部分或者属性名包含有非法字符时（例如来自 json_decode() 或 SimpleXML）。

**示例 \#1 可变属性示例**

``` php
<?php
class Foo {
    public $bar = 'I am bar.';
    public $arr = ['I am A.', 'I am B.', 'I am C.'];
    public $r   = 'I am r.';
}

$foo = new Foo();
$bar = 'bar';
$baz = ['foo', 'bar', 'baz', 'quux'];
echo $foo->$bar . "\n";
echo $foo->{$baz[1]} . "\n";

$start = 'b';
$end   = 'ar';
echo $foo->{$start . $end} . "\n";

$arr = 'arr';
echo $foo->{$arr[1]} . "\n";
echo $foo->{$arr}[1] . "\n";

?>
```

以上示例会输出：

    I am bar.
    I am bar.
    I am bar.
    I am r.
    I am B.

**警告**

注意，在 PHP 的函数和类的方法中，超全局变量不能用作可变变量。`$this` 变量也是一个特殊变量，不能被动态引用。

---

## [S3.4] 預定義變數

- url: https://www.php.net/manual/zh/language.variables.predefined.php
- fidelity: verbatim
- fetched: 2026-11-22

## 预定义变量

PHP 提供了许多 预定义变量。PHP 提供了一套附加的预定数组，这些数组变量包含了来自 web 服务器（如果可用），运行环境，和用户输入的数据。这些数组在每个作用域内自动可用。因此通常被称为自动全局变量（autoglobals）或者超全局变量（superglobals）。（PHP 中没有用户自定义超全局变量的机制。）详情参阅超全局变量列表。

> **注意**: **可变变量**  
>
> 超级全局变量不能被用作函数或类方法中的可变变量。

如果某些 variables_order 中的变量没有设定，它们的对应的 PHP 预定义数组也是空的。
