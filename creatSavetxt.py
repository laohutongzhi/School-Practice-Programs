# -*- encoding: UTF-8 -*-

from pathlib import Path

def saveed():
    with open("学生信息.txt", mode = "w", encoding = "utf-8") as f:
        f.write("姓名：张三\n")
        f.write("学号：2026123456\n")

def saveInput(): 
    path = Path(str(input("输入保存路径：")))
    while path:
        if path.is_dir():
            path = path / "成绩单.txt"
            print("文件将保存在：{}".format(path))
            break
        else:
            path = Path(str(input("有错，输入保存路径：")))
    name = str(input("请输入姓名："))
    number = str(input("请输入学号："))
    Chinese = str(input("输入语文成绩："))
    Mathematics = str(input("输入数学成绩："))
    English = str(input("输入英语成绩："))
    with open(path, mode = "w", encoding = "utf-8") as f:
        f.write("姓名：{}\n".format(name))
        f.write("学号：{}\n".format(number))
        f.write("语文成绩：{}\n".format(Chinese))
        f.write("数学成绩：{}\n".format(Mathematics))
        f.write("英语成绩：{}\n".format(English))
    print("写入完毕")


def printAsShit():
    name = str(input("输入姓名："))
    age = str(input("输入年龄："))
    city = str(input("输入城市："))
    print(  "**********",
            "姓名：" + name,
            "年龄：" + age,
            "城市：" + city,
            "**********", sep="\n")


def printAsPoem():
    Poem = []
    Marks = ["，", "。"]
    Poem.append(str(input("写一行诗：")))
    Poem.append(str(input("再写一行：")))
    Poem.append(str(input("又写一行：")))
    Poem.append(str(input("最后一行：")))
    for i in range(4):
        print(Poem[i] + Marks[i % 2])


def main():
    pass

if __name__ == "__main__":
    main()
