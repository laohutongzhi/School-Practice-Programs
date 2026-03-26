year = int(input("输入一个一个一个年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:      # 年份能被4整除且不能被100整除，或者能被400整除视为闰年
    print(year, "年是闰年")
else:
    print(year, "年是平年")
