import socket #客户端操作

HOST = "10.10.10.234"
POST = 5000
addr = (HOST,POST)  #要连接对方主机

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(addr)  #连接对方主机
def sendfile():
    data = c.recv(1024) #等待对方说可以发送
    print(str(data,encoding="gbk"))
    file = input("请输入你想发送的文件：") #文件路径要用\\分割
    filename = file.split("\\")[-1]  #取出文件名称
    #print(filename)
    c.send(bytes(filename,encoding="gbk"))
    with open(file,"rb") as f:
        fdata = f.read()  #读取文件内容
    c.send(fdata)   #发送文件内容
    data2 = c.recv(1024)  #收到对方提示的完成信息
    print(str(data2,encoding="gbk"))

def getfile():
    data = c.recv(1024) #等待对方说可以发送
    print(str(data,encoding="gbk"))
    file = input("请输入你想下载的文件：") #文件路径要用\\分割
    c.send(bytes(file,encoding="gbk"))
    filename = file.split("\\")[-1]  #定义对方的文件名
    fdata = c.recv(1024)
    with open(filename,"wb") as f:
        f.write(fdata)
    data2 = c.recv(1024)
    print(str(data2,encoding="gbk"))

    
def main(addr):
    
    while True:
        cmd = input("请输入发送内容：")
        c.send(bytes(cmd,encoding="gbk")) #发送内容转换
        
        if cmd == "quit":
            break
        if cmd == "sendfile":
            sendfile()
            continue
        if cmd == "getfile":
            getfile()
            continue
        data = c.recv(1024)  #一次接收的数据量
        print(str(data,encoding="gbk"))
    c.close()

if __name__ == "__main__":
    main(addr)
