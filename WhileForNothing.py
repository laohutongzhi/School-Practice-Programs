# -*- encoding: UTF-8 -*-

def whilecal100():      #使用 while 循环，计算输出1+2+…+100的和
    i = 1
    sumnum = 0
    while i <= 100:
        sumnum += i
        i += 1
    return sumnum


def forcal100():        #使用 for 循环，计算输出1+2+…+100的和
    sumnum = 0
    for i in range(100):
        sumnum += i + 1
    return sumnum


def whileprinteven(i):      #使用 while 循环，输出1—100之间所有偶数
    j = 0
    while j <= i:
        print(j)
        j += 2


def forprinteven(i):        #使用 for 循环，输出1—100之间所有偶数
    for j in range(0, i + 1, 2):
        print(j)


def whileLCM(a, b):     #使用 while 循环，输入两个正整数，输出最小公倍数
    lcm = max(a, b)
    while lcm <= a * b:
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        else:
            lcm += 1


def forLCM(a, b):       #使用 for 循环，输入两个正整数，输出最小公倍数
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i
