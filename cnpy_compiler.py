import re
import sys
import os
import tokenize
from io import BytesIO

DEFAULT_SYNTAX = {
    "关键词": {
        "如果": "if",
        "否则": "else",
        "对于": "for",
        "在": "in",
        "定义": "def",
        "返回": "return",
        "真": "True",
        "假": "False",
        "空": "None",
    },
    "运算符": {"并且": "and", "或者": "or", "非": "not"},
    "内置函数": {"打印": "print", "范围": "range"},
}


class CNPyCompiler:
    def __init__(self, syntax_dict=None):
        self.syntax_dict = syntax_dict or DEFAULT_SYNTAX
        self.replacements = self._build_replacements()

    def _build_replacements(self):
        replacements = {}
        for category in self.syntax_dict:
            for cn, en in self.syntax_dict[category].items():
                replacements[cn] = en
        return replacements

    def translate(self, cn_code):
        def replace(match):
            return self.replacements.get(match.group(0), match.group(0))

        pattern = re.compile(
            "|".join(
                re.escape(cn) for cn in sorted(self.replacements, key=len, reverse=True)
            )
        )
        return pattern.sub(replace, cn_code)

    def compile_to_py(self, source_file, output_file=None):
        if not source_file.endswith(".cnpy"):
            raise ValueError("源文件必须是.cnpy扩展名")

        with open(source_file, "r", encoding="utf-8") as f:
            cn_code = f.read()

        py_code = self.translate(cn_code)

        if output_file is None:
            output_file = source_file.replace(".cnpy", ".py")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(py_code)

        print(f"编译完成: {source_file} -> {output_file}")
        return output_file

    def execute(self, source_file):
        py_file = self.compile_to_py(source_file)
        try:
            with open(py_file, "r", encoding="utf-8") as f:
                code = compile(f.read(), py_file, "exec")
            exec(code)
        except Exception as e:
            print(f"执行错误: {e}")


def main():
    if len(sys.argv) < 2:
        print("用法: cnpy 文件.cnpy")
        return

    compiler = CNPyCompiler()
    source_file = sys.argv[1]
    compiler.execute(source_file)


if __name__ == "__main__":
    main()
