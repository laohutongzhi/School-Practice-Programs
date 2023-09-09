#注释只是懒得写罢了
#程序报过两次错，然后我也不知道为什么反正修好了
#果然一份代码要是能跑就不要去动它
#原神，启动！！！
from random import randint
num=randint(1,999)
time=0
max=999
min=1
running=True
while running:
    minstr=str(min)
    maxstr=str(max)
    print("猜一个"+minstr+"至"+maxstr+"之间的整数")
    guess=int(input("请输入："))
    if guess==num:
        time=time+1
        print("正确，已猜",time,"次")
        running=False
    elif guess<num:
        if guess>min:
            min=guess
            time=time+1
            print("太小，已猜",time,"次")
        else:
            print("请输入",min,"至",max,"之间的整数！！")
    else:
        if guess<max:
            max=guess
            time=time+1
            print("太大，已猜",time,"次")
        else:
            print("请输入",min,"至",max,"之间的整数！！")
