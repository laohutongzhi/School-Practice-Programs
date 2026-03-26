# -*- coding: utf-8 -*-

def cal(a ,b ,c):
    ifu = b ** 2 - 4 * a * c
    if ifu > 0:         # 如果判别式大于0，说明方程有两个不同的实数解
        x1 = (-b + ifu ** 0.5) / (2 * a)
        x2 = (-b - ifu ** 0.5) / (2 * a)
    elif ifu == 0:      # 如果判别式等于0，说明方程有两个相同的实数解
        x1 = x2 = -b / (2 * a)
    else:               # 如果判别式小于0，说明方程无实数解
        return 0, 0,False
    return x1, x2, True

if __name__ == "__main__":
    # 输入a, b, c的值
    print("输入ax^2+bx+c=0")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    x1, x2, flag = cal(a, b, c)     # 计算方程的解
    # 输出结果
    if flag:
        if x1 != x2:
            print("方程的解为：x1 = %s, x2 = %s" % (x1, x2))
        else:
            print("方程的解为：x1 = x2 = %s" % x1)
    else:
        print("方程无实数解")