def list20():  # 定义一个列表，将2~20中的偶数存入，并完成输出
    lst = [x for x in range(2, 21, 2)]
    return lst


def createlist(round: int = 10) -> list:  # 输入10个数存入列表中
    lst = []
    inputnum = str(input("输入数字："))
    while round > 0:
        if inputnum.isdigit():
            lst.append(int(inputnum))
            round -= 1
        else:
            print("输入有误")
        if round > 0:
            inputnum = str(input("输入数字："))
    return lst


def createlistonce(volume: int = 10) -> list:  # 输入10个数存入列表中
    lst = str(input("输入{}个数字，以空格分隔：\n".format(volume))).split(" ")
    while len(lst) != volume:
        print("输入有误，再次输入")
        lst = str(input("输入{}个数字，以空格分隔：\n".format(volume))).split(" ")
    return lst


def listsum():  # 输入10个数存入列表中，将其中数求和
    lst = createlist()
    return sum(lst)


def listmin():  # 输入10个数存入列表中，找出其中最小值
    lst = createlist()
    return min(lst)


def listnmax(n: int):  # 输入n个数存入列表中，找出其中最大值
    lst = createlist(n)
    return max(lst)


def fibonacci30():  # 将斐波那契数列的前30个存入列表中
    seq = [0, 1]
    for i in range(2, 30):
        seq.append(seq[i - 2] + seq[i - 1])
    return seq


def printfibonacci():  # 将斐波那契数列的前30个存入列表中，并完成每行五个的输出
    seq = fibonacci30()
    for i in range(0, len(seq), 5):
        print(
            "{0:5d} {1:6d} {2:6d} {3:6d} {4:6d}".format(
                seq[i], seq[i + 1], seq[i + 2], seq[i + 3], seq[i + 4]
            )
        )


def listreverse():  # 从键盘输入10个数，存入列表，然后将列表中的10个数居中对称互换
    lst = createlist()
    return lst[::-1]


def listrevdersenew():  # 从键盘输入10个数，存入列表，然后将列表中的10个数居中对称互换
    lst = createlist()
    lst.reverse()
    return lst


def listsort5():  # 从键盘输入5个整数，按升序（由小到大）进行排序。
    lst = createlistonce(5)
    lst.sort()
    return lst


if __name__ == "__main__":
    pass
