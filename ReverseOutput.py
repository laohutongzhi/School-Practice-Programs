# -*- coding: utf-8 -*-

"""给定一个整数，将该数各个位上数字反转得到一个新数。
新数满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零
"""


strin = str(input("输入数字："))
if strin[0] == '-':
    strin = strin[1:]
    intout = -int(strin[::-1])
else:
    intout = int(strin[::-1])
print("倒序输出：", intout)