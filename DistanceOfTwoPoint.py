firstPoint = str(input("请输入第一个点：（格式：x，y)\n"))
secondPoint = str(input("请输入第二个点：（格式：x，y)\n"))

# 拆分出点坐标

if "," in firstPoint:
    x1y1 = firstPoint.split(",", 1)
elif "，" in firstPoint:
    x1y1 = firstPoint.split("，", 1)
else:
    x1y1 = ""
    print("输入有误！")
    exit()

if "," in secondPoint:
    x2y2 = secondPoint.split(",", 1)
elif "，" in secondPoint:
    x2y2 = secondPoint.split("，", 1)
else:
    x2y2 = ""
    print("输入有误！")
    exit()

x1, y1 = int(x1y1[0]), int(x1y1[1])
x2, y2 = int(x2y2[0]), int(x2y2[1])

# 计算坐标距离
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("两点间的距离为：", distance)
