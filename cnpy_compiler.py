import json
import re
import sys


def compile_cnpy(source_file, output_file):
    # 加载语法字典
    with open('cnpy_dict.json', 'r', encoding='utf-8') as f:
        syntax_dict = json.load(f)

    # 合并所有替换规则
    replacements = {}
    for category in syntax_dict:
        replacements.update(syntax_dict[category])

    # 读取中文代码
    with open(source_file, 'r', encoding='utf-8') as f:
        cn_code = f.read()

    # 按优先级排序替换（长关键词优先）
    sorted_keys = sorted(replacements.keys(), key=len, reverse=True)

    # 执行替换（保留字符串常量）
    py_code = cn_code
    for cn_key in sorted_keys:
        en_val = replacements[cn_key]
        # 使用正则避免替换字符串内的内容
        py_code = re.sub(
            r'\b' + re.escape(cn_key) + r'\b',
            en_val,
            py_code
        )

    # 写入标准Python文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(py_code)

    print(f"编译完成: {source_file} -> {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python cnpy_compiler.py 输入.cnpy 输出.py")
        sys.exit(1)

    compile_cnpy(sys.argv[1], sys.argv[2])