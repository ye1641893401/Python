userdict = {'bob':'444','tom':'123'}

username = input("请输入用户名：")
password = input("请输入密码：")
if username in userdict.keys() and password == userdict[username]:
    print("欢迎"+username+"用户登录")
else:
    print("你输入的用户名或者密码有误")
