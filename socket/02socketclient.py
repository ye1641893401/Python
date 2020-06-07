import socket

HOST = "10.10.10.234"
POST = 5000
addr = (HOST,POST)

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def main(addr):
    c.connect(addr)
    while True:
        cmd = input("请输入发送内容：")
        c.send(bytes(cmd,encoding="gbk"))
        data = c.recv(1024)
        print(str(data,encoding="gbk"))
        if cmd == "quit":
            break
    c.close()

if __name__ == "__main__":
    main(addr)
