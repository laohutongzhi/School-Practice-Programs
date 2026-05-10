# -*- encoding: UTF-8 -*-

"""
一球从high米高空自由落下，每次落地后反跳回原高度的一半，再落下，
求它在第time次落地时，共经过了多少米，第time次反弹多高
"""

high = 100
time = 10
distance = -high
for i in range(1, time + 1):
    distance += high * 2
    high /= 2
print("在第{}次落地时，共经过了{}米，第{}次反弹{}米".format(time, distance, time, high))
