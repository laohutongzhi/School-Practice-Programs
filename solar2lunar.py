# solar2lunar
"""
输入一个公历年份时，输出对应的农历年。
"""

Stems = "甲乙丙丁戊己庚辛壬癸"
Branches = "子丑寅卯辰巳午未申酉戌亥"
zodiac_signs = "鼠牛虎兔龙蛇马羊猴鸡狗猪"


def solor2lunar(solor: int) -> str:
    lunar = ""
    solor -= 3
    lunar += Stems[solor % 10 - 1]
    lunar += Branches[solor % 12 - 1] + zodiac_signs[solor % 12 - 1]
    return lunar + "年"


if __name__ == "__main__":
    solor = int(input("输入一个公历年份："))
    lunar = solor2lunar(solor)
    print(f"{solor}年是{lunar}")
