# -*- encoding: utf-8 -*-

"""
读入一系列整数，统计出正整数个数i和负整数个数j,读入0则结束。
"""


input_str = float(input("请输入："))
i = 0
j = 0
while input_str != 0:
    if input_str == int(input_str):
        if input_str > 0:
            i += 1
        elif input_str < 0:
            j += 1
    input_str = float(input("请输入："))
print("正整数个数：%d，负整数个数：%d" % (i, j))