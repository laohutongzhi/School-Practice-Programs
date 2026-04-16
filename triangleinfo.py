# -*- encoding: UTF-8 -*-

"""
根据输入的三角形的三边判断是否能组成三角形，
若可以构成三角形则输出它的面积和三角形的类型（等边、等腰、直角）。
"""


def length_num(length_list):
    length = []
    for i in length_list:
        length.append(int(i))
    return length


def istriangle(length_list):
    if length_list[0] + length_list[1] >= length_list[2] and \
            length_list[0] + length_list[2] >= length_list[1] and \
            length_list[2] + length_list[1] >= length_list[0]:
        return True
    else:
        return False


def type_of_triangle(length_list):
    tritype = ""
    if length_list[0] == length_list[1] and \
            length_list[0] == length_list[2] and \
            length_list[1] == length_list[2]:
        tritype = "等边三角形"
    elif length_list[0] == length_list[1] or \
            length_list[0] == length_list[2] or \
            length_list[1] == length_list[2]:
        tritype = "等腰三角形"
    if length_list[0] ** 2 + length_list[1] ** 2 == length_list[2] ** 2 or \
            length_list[0] ** 2 + length_list[1] ** 2 == length_list[2] ** 2 or \
            length_list[0] ** 2 + length_list[1] ** 2 == length_list[2] ** 2:
        if tritype:
            tritype = "等腰直角三角形"
        else:
            tritype = "直角三角形"
    return tritype


def main():
    length_list = str(input("输入三角形三条边边长，用空格分隔：")).split(" ")
    length_list = length_num(length_list)
    if istriangle(length_list):
        print("可以组成三角形")
        print(type_of_triangle(length_list))
    else:
        print("不能组成三角形")


if __name__ == "__main__":
    main()
