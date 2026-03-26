# -*- encoding: UTF-8 -*-

def CtoF(C):    # 摄氏度（°C）转换为华氏度（°F）的公式是：°F = °C × 9/5 + 32
    F = C * 9 / 5 + 32
    return F


if __name__ == "__main__":
    C = float(input("请输入一个摄氏度："))
    F = CtoF(C)
    print("华氏度为：", F)
