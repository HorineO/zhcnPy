# 测试中文 Python 代码

def 阶乘(n):
    if n == 0:
        return 1
    else:
        return n * 阶乘(n - 1)

print("5的阶乘是", 阶乘(5))