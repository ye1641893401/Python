try:
    f = open(r"c:\users\allen\test.txt","wb")
    num = input("请输入值：")
    f.write(num)
except (KeyboardInterrupt,EOFError):
    print("quit")
finally:
    f.close()
    print(f.closed)
