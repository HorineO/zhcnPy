# zhcnPy: 中文 Python 编译器

`zhcnPy` 是一个简单的中文 Python 编译器，它允许你使用中文关键字、运算符和内置函数编写 Python 代码。该编译器将中文代码翻译成标准的 Python 代码，然后执行。

## 功能

- **中文编程**: 使用熟悉的中文词汇编写 Python 代码。
- **易于扩展**: 可以通过修改 `cnpy_dict.json` 文件轻松添加或修改语法映射。
- **编译和执行**: 将 `.cnpy` 文件编译为 `.py` 文件，并可以直接执行编译后的文件。

## 安装

无需特殊安装。只需将 `cnpy_compiler.py` 和 `cnpy_dict.json` 文件放在同一目录下即可。

## 使用方法

### 编译 `.cnpy` 文件

要将 `.cnpy` 文件编译为 `.py` 文件，请运行：

```bash
python cnpy_compiler.py your_file.cnpy
```

这将在同一目录下生成一个名为 `your_file.py` 的 Python 文件。

### 执行 `.cnpy` 文件

要直接执行 `.cnpy` 文件（这将自动编译并运行），请运行：

```bash
python cnpy_compiler.py your_file.cnpy
```

## 示例

假设你有一个名为 `test.cnpy` 的文件，内容如下：

```cnpy
定义 打印数字(范围_结束):
    对于 数字 在 范围(范围_结束):
        如果 数字 % 2 非 空:
            打印("奇数:", 数字)
        否则:
            打印("偶数:", 数字)

打印数字(10)
```

运行 `python cnpy_compiler.py test.cnpy` 后，它将被编译为 `test.py`：

```python
def print_numbers(range_end):
    for number in range(range_end):
        if number % 2 is not None:
            print("Odd:", number)
        else:
            print("Even:", number)

print_numbers(10)
```

并执行输出：

```
偶数: 0
奇数: 1
偶数: 2
奇数: 3
偶数: 4
奇数: 5
偶数: 6
奇数: 7
偶数: 8
奇数: 9
```

## 语法映射

以下是 `zhcnPy` 当前支持的中文到英文的语法映射：

### 关键词

| 中文 | 英文   |
| :--- | :----- |
| 如果 | if     |
| 否则 | else   |
| 对于 | for    |
| 在   | in     |
| 定义 | def    |
| 返回 | return |
| 真   | True   |
| 假   | False  |
| 空   | None   |

### 运算符

| 中文 | 英文 |
| :--- | :--- |
| 并且 | and  |
| 或者 | or   |
| 非   | not  |

### 内置函数

| 中文 | 英文  |
| :--- | :---- |
| 打印 | print |
| 范围 | range |
