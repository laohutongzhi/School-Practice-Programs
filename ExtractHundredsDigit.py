numin = str(input("输入："))
if len(numin) < 4:
    numin = (4-len(numin))*"0"+numin
elif len(numin) > 4:
    numin = numin[-4:]
numout = numin[1]
print("百位是：", numout)
