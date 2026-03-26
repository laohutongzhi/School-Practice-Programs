# -*- coding: utf-8 -*-
# 输入
while True:
    print("地球上现有资源加上新生资源可供")
    x = int(input("几亿人："))
    a = int(input("活几年："))
    print("或者")
    y = int(input("几亿人："))
    b = int(input("活几年："))
    print("正在验算...")
    if (x > y and a < b and a * x < b * y) and \
            (a < 10000 and x < 10000 and b < 10000 and y < 10000):
        print("数据没有问题！")
        break
    else:
        print("数据有问题！再输一遍！")

# 计算程序
z = round((x * a - y * b) / (a - b), 2)

# 输出
print("为了能够实现可持续发展，避免资源枯竭，地球最多能够养活", z, "亿人")
