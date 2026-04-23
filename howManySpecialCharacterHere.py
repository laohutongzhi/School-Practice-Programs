# -*- encoding: UTF-8 -*-
"""从键盘键入一行字符，
分别统计并输出其中大写英文字符、小写英文字符、中文字符、数字和其它字符的个数
"""

inputstr = str(input("输入点什么："))
uppercharacter = 0
lowercharacter = 0
chinesecharacter = 0
arabicnumerals = 0
othercharacter = 0
for i in inputstr:
    if i.isupper():
        uppercharacter += 1
    elif i.islower():
        lowercharacter += 1
    elif '\u4e00' <= i <= '\u9fff':
        chinesecharacter += 1
    elif i.isdigit():
        arabicnumerals += 1
    else:
        othercharacter += 1
print("大写英文个数为", uppercharacter)
print("小写英文个数为", lowercharacter)
print("中文字符个数为", chinesecharacter)
print("数字字符个数为", arabicnumerals)
print("其他字符个数为", othercharacter)
