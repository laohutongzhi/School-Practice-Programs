#dodge是躲闪
#curing是治疗
from random import randint  #载入randit模块
playerblood=1000    #设置玩家血量
monsterblood=1000   #设置怪兽血量
running=True    #设置运行为正确
while running:
    if playerblood>0:   #检查玩家是否被击败
        playerblood_s=playerblood//50   #将玩家血量转换为百分比
        monsterblood_s=monsterblood//50 #将怪兽血量转换为百分比
        print("你的血量："+"■"*playerblood_s,"◻"*(20-playerblood_s))
        print("怪兽血量："+"■"*monsterblood_s,"◻"*(20-monsterblood_s))
        print("1:究极无敌吊炸天之冰霜术")
        print("2:超级无敌伤害高之火球术")
        print("3:回的没有掉的多之治疗术")
        print("4:有概率一刀999之搏一搏")
        player_skill=int(input("输入技能编号："))
        dodge=randint(1,100)
        if player_skill==1:    #技能一
            print("使用了 究极无敌吊炸天之冰霜术！")
            if dodge<=80:    #击中概率80%
                harm=randint(200,300)   #冰霜术伤害200-300
                monsterblood=monsterblood-harm
                print("怪兽受到",harm,"点伤害！")
            else:
                print("怪兽大jio一抬躲过去了")
        elif player_skill==2:  #技能二
            print("使用了 超级无敌伤害高之火球术！")
            if dodge<=60:   #击中概率60%
                harm=randint(300,400)   #火球术伤害300-400
                monsterblood=monsterblood-harm
                print("怪兽受到",harm,"点伤害！")
            else:
                print("怪兽脖子一扭躲过去了")
        elif player_skill==3:  #技能三
            print("使用了 回的没有掉的多之治疗术！")
            curing=randint(200,400)     #治疗术回血200-400
            playerblood=playerblood+curing
            print("治疗使你恢复了",curing,"点血量")
        elif player_skill==4:  #技能四
            print("使用了 有概率一刀999之搏一搏")
            if dodge<=90:   #失败概率90%
                monsterblood=monsterblood-1
                print("你打出了高达 1 点的伤害！！！")
            else:   #成功
                monsterblood=monsterblood-999
                print("你打出了高达 999 点的伤害！！！")
        else:   #技能输入有误
            print("你TM输入的什么玩意儿")
    else:
        print("死了啦，都是你害的")
        running=False
    if monsterblood>0:  #检查怪兽是否被击败
        monster_skill=randint(1,3)
        dodge=randint(1,100)
        if monster_skill==1:    #怪兽使用技能一
            print("怪兽使用了跺jiojio")
            if dodge>=60:   #击中概率60%
                harm=randint(300,400)   #跺jiojio伤害300-400
                playerblood=playerblood-harm
                print("你受到",harm,"点伤害！")
            else:
                print("你向上一跳，躲开了")
        elif monster_skill==2:  #怪兽使用技能二
            print("怪兽给了你一巴掌")
            if dodge>=70:   #击中概率70%
                harm=randint(400,500)   #一巴掌伤害400-500
                playerblood=playerblood-harm
                print("你受到",harm,"点伤害！")
            else:
                print("你向后一跃，躲开了")
        else:   #怪兽使用技能三
            curing=randint(200,400)
            monsterblood=monsterblood+curing
            print("怪兽使用了治疗术，回复了",curing,"点血")
        if playerblood>1000:    #检查玩家血量是否超过上限
            playerblood=1000    #超过后复原
        if monsterblood>1000:   #检查怪兽血量是否超过上限
            monsterblood=1000   #超过后复原
    else:
        print("你太硬了，怪兽被你干死了")
        running=False
    if playerblood<0:   #检查玩家是否被击败
        print("死了啦，都是你害的")
        running=False
input("......")
