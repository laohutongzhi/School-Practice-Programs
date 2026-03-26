flo = float(input("请输入一个小数："))

integerPart = int(flo)                      # 整数部分
decimalPart = flo - int(flo)                # 小数部分
roundDecimalPart = round(decimalPart, 3)    # 保留3位小数

print("整数部分是：", integerPart)
print("小数部分是：", roundDecimalPart)
