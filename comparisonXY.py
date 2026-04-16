# -*- encoding: UTF-8 -*-

list1 = str(input("输入 x, y ，以空格分隔：")).split(" ")
list1[0] = int(list[0])
list1[1] = int(list1[1])
if list1[0] < list1[1]:
    print(list1[0], "<", list1[1])
elif list1[0] > list1[1]:
    print(list1[0], ">", list1[1])
else:
    print(list1[0], "=", list1[1])