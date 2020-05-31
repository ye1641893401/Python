def ex(anum,bnum):
    cnum = anum / bnum
    return cnum

if __name__ == "__main__":
    try:
        anum = int(input("请输入被除数："))
        bnum = int(input("请输入除数："))
        data = ex(anum,bnum)
        print(data)
    except (KeyboardInterrupt,EOFError):
        print("退出")
    except ValueError:
        print("请输入数字")
    except ZeroDivisionError as e:
        print(e)
