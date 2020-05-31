"""
这是一个测试的函数讲解实例
20181229作者allen
"""

def pri_ban(num=30):
    "我的功能是打印20个井号"
    return ("*" * num)

if __name__ == "__main__":
    "当作为程序运行时候下面代码执行，如果当模块调用下面代码不执行"
    data = pri_ban(10)
    print(data)
