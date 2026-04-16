# -*- encoding: UTF-8 -*-

"""
找到自行车，开锁并车上自行车的时间为27秒，停车锁车的时间为23秒；
步行每秒行走1.2米，骑车每秒行走3.0米。
判断走不同的距离去办事,是骑车快还是走路快。
如果骑车快，输出一行"Bike"；如果走路快，输出一行"Walk"；如果一样快，输出一行"All"。
输入:
    输入一行，包含一个整数，表示一次办事要行走的距离,单位为米。
输出:
    输出一行,如果骑车快,输出一行"Bike";如果走路快,输出一行"Walk";如果一样快,输出一行"All"。
"""


def main():
    distance = float(input("输入这次办事要行走的距离："))
    bike_time = 27 + 23 + distance / 3.0
    walk_time = distance / 1.2
    if bike_time > walk_time:
        print("Walk")
    elif bike_time < walk_time:
        print("Bike")
    else:
        print("All")


if __name__ == "__main__":
    main()
