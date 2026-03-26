instr = str(input("输入小写英文字母："))
outstr = ""
for i in instr:         # 遍历字符串
    if i.isalpha():     # 判断是否为字母
        outstr += i     # 是则加入
print("大写是：", outstr.upper())