# -*- coding: utf-8 -*-

"""
输入两个正整数m和k，其中1<m<100000，1<k<5 ，
判断m 能否被19整除，且恰好含有k个3，
如果满足条件，则输出YES，否则，输出NO。
"""

m = str(input("请输入正整数m："))
k = int(input("请输入正整数k："))

for i in m:
    if i == '3':
        k -= 1
if int(m) % 19 == 0 and k == 0:
    print("YES")
else:
    print("NO")