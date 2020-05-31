import random


wincount = 0
lostcount = 0
cholist = ["锤子","剪刀","布"]

while True:
    pchonum = input("请输入0\锤子,1\剪刀,2\布：")
    pcho = cholist[int(pchonum)]
    "利用角标的形式调用列表中的值"
    ccho = random.choice(cholist)

    print("你输入的是%s,计算机输入的是%s" %(pcho,ccho))

    if (pcho == "锤子" and  ccho == "剪刀") or (pcho == "剪刀" and  ccho == "布") \
       or (pcho == "布" and  ccho == "锤子"):
        print("恭喜你赢了")
        wincount += 1 
    elif pcho == ccho:
        print("平局")
    else:
        print("你输了")
        lostcount += 1

    if wincount == 2 or lostcount == 2:
        break
