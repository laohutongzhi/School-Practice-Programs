from random import randint
Bout=int(input("请输入要生成的次数："))
DiceList=[]
for chart in range(Bout):
    FirstDice=randint(1,6)
    print("第一个骰子投出了"+str(FirstDice)+"！")
    SecondDice=randint(1,6)
    print("第二个骰子投出了"+str(SecondDice)+"！")
    FixedNumber=FirstDice+SecondDice
    print("相加等于"+str(FixedNumber))
    FixedNumber=FixedNumber-1
    print("这张谱面的定数是"+str(FixedNumber)+"！")
    DiceList.append(FixedNumber)
print()
print("以下为谱面定数")
print("----------------------------------------")
for cnmBuXiangQuMingLe in range(Bout):
    print("第"+str(cnmBuXiangQuMingLe+1)+"个谱面定数为"+str(DiceList[cnmBuXiangQuMingLe]))
END=input()     #是的结束了你还想看什么？