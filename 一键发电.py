from tkinter import Tk

def copy_to_clipboard(text):
    root = Tk()
    # 隐藏主窗口
    root.withdraw()
    # 清空剪贴板
    root.clipboard_append(text)
    # 更新剪贴板
    root.update()
    # 销毁Tk对象
    root.destroy()

def choice_list():
    print("1. ♡…… 嘿嘿嘿")
    print("2. 情况不太妙")


while True:
    choice_list()
    choice=input("选择：")
    dian=str(input("Enter a name: "))
    if choice=="1":
        text="♡…… 嘿嘿嘿我的"+dian+"♡…… 已经离不开"+dian+"了…… 世界上怎么会有"+dian+"这么完美的人…… 嘿嘿我的"+dian+"♡… 已经不能再忍受了…♡最、最喜欢"+dian+"了！…♡像个笨蛋一样♡… 一直、一直都在忍受着对"+dian+"的爱…♡心里一直都是"+dian+"！♡我真的、真的很♡"+dian+"…♡呜呜… "+dian+"、"+dian+"的样子已经被我深深的刻在心里了！…♡是、是的...♡喜欢"+dian+"！我真的喜欢"+dian+"！........♡呜呜、不行了，我已经变成不看"+dian+"就不行的笨蛋了... 啊啊♡好喜欢♡"+dian+"…"
    elif choice=="2":
        text="情况不太妙。如果我想要我的生活步入正轨，退坑是我能想到的唯一的解决方案。这是我能过上更好生活的最后手段。我已经对"+dian+"上瘾了，它对我的生活造成了影响，我的社交生活，我的潜力，我的未来都会在眨眼间消失。趁我还可以的时候，我需要走出去去寻找一些新的东西。"
    print(text)
    copy_to_clipboard(text)
