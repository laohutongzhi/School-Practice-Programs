# -*- encoding: UTF-8 -*-

"""
十个小孩围成一圈分糖果，
老师分给第一个小孩10块，
    第二个小孩2块，
    第三个小孩8块，
    第四个小孩22块，
    第五个小孩16块，
    第六个小孩4块，
    第七个小孩10块，
    第八个小孩6块，
    第九个小孩14块，
    第十个小孩20块。
然后所有的小孩同时将手中的糖分一半给右边的小孩；
糖块数为奇数的人可向老师要一块。
问经过这样几次后大家手中的糖的块数一样多
    每人各有多少块糖
"""

list1 = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]
list2 = list1.copy()
flag = 1
roundn = 0


def allsame(lst):
    for i in range(len(lst) - 1):
        if lst[i] != lst[1 + 1]:
            return False
    return True


while not allsame(list1):
    if flag == 1:
        for i in range(len(list1) - 1):
            list2[i + 1] = int((list1[i] + list2[i + 1] + 1) // 2)
        list2[0] = int((list1[-1] + list2[0] + 1) // 2)
        list1 = list2.copy()
    elif flag == -1:
        for i in range(len(list1) - 1):
            list1[i + 1] = int((list2[i] + list1[i + 1] + 1) // 2)
        list1[0] = int((list2[-1] + list1[0] + 1) // 2)
        list2 = list1.copy()
    flag = -flag
    roundn += 1

print(roundn, "次后大家手中的糖的块数一样多")
print("每人各有{}块糖".format(list1[0]))
