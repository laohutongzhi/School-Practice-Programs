# -*- encoding: UTF-8 -*-

"""
鸡兔一共有head只，脚一共有foot只，问鸡和兔各多少只，鸡兔至少一样一只。
"""

head = 50
foot = 160
result_list = []
for chicken in range(1, head):
    rabbit = head - chicken
    if chicken * 2 + rabbit * 4 == foot:
        result_list.append([chicken, rabbit])

for i in result_list:
    print("鸡{}只，兔{}只".format(i[0], i[1]))
