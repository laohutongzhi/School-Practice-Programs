# -*- encoding: utf-8 -*-
"""
每本书的单价分别为：3.1，1.7，2，5.3，0.9和7.2。
从六本书中选出若干本，使得单价相加所得的和同10最接近。
"""

books = [3.1, 1.7, 2, 5.3, 0.9, 7.2]
round = 2 ** len(books)
aim = 10
closest = []
closest_choice = []


def dec2bin(num):
    # 将十进制数转为二进制位列表，高位在前。
    l = []
    while True:
        remainder = num % 2
        num = num // 2
        l.append(remainder)
        if num == 0:
            return l[::-1]


def reform_choice(choice):
    # 补齐选择列表到6位（使用0填充）。
    choice = [0] * (6 - len(choice)) + choice
    return choice


def count_price(choice):
    # 根据选择计算总价。
    price = 0
    for i in range(len(choice)):
        price += books[i] * choice[i]
    return price


def closest_try(price, choice):
    # 更新并保存当前最接近目标的组合。
    if not closest:
        closest.append(price)
        closest_choice.append(choice)
    elif abs(aim - closest[-1]) > abs(aim - price):
        closest.clear()
        closest_choice.clear()
        closest.append(price)
        closest_choice.append(choice)
    elif abs(aim - closest[-1]) == abs(aim - price):
        closest.append(price)
        closest_choice.append(choice)
    return closest, closest_choice


for i in range(round):
    # 枚举所有可能的选择组合
    choice = reform_choice(dec2bin(i))
    price = count_price(choice)
    closest, closest_choice = closest_try(price, choice)

for i in range(len(closest)):
    # 输出最接近目标的选择和对应价格
    print("选择为{}，价格是{}".format(closest_choice[i], closest[i]))
