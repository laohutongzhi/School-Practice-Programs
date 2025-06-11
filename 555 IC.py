#-*- coding: utf-8 -*-                                                                                                       

def IC_555(Vcc,P2,P3,P6,P4=1,P5=-1,):
    if P5==-1:  #5脚未使用
        P5=Vcc*2/3
    if P4==0:    #啷个还消思考，没启用芯片
        P3=0
        P7=True
    else:
        if P2<P5/2:    #老二一眼盯真
            P3=1
            P7=False
        else:   #坏了，老二被过了
            if P6>P5:   #老六殿后，两手准备
                P3=0
                P7=True
            else:    #保持状态，彻底没戏
                P3=P3
                P7=P3==0
    return P3,P7

if __name__ == '__main__':
    Vcc=input("请输入电压：")
    P2=input("请输入P2电位：")
    P3=input("请输入P3电位：")
    P4=input("请输入P4电位：")
    P5=input("请输入P5电位：")
    P6=input("请输入P6电位：")
    P3,P7=IC_555(Vcc,P2,P3,P6,P4,P5)
    print(P3,P7)