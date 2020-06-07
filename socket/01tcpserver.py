 服务端   关机 shutdown -s -t 0
import socket

HOST = "10.10.10.234"
POST = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,POST))
s.listen(1)
conn,addr = s.accept()
print(addr)
data = conn.recv(1024)
print(data)

conn.close()
s.close()
