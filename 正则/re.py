192.168.0.10      AC 48 94 5D A9 3A
192.168.0.11      FB 55 A6 3F A7 4B
192.168.0.12      A9 68 95 6B CC 1D 

import re

m = re.sub(n"(..)(..)(..)(..)(..)(..)(..)(..)\r\n","rb\1:2:3:4:5:6:7\r\n",data)
print (m)


先用open函数打开文件以rb读取的方式打开并赋值
f = open(r"ipmaclist.txt","rb")
data = f.read()
m = re.sub(b"(..) (..) (..) (..) (..) (..)\r\n",rb"\1:\2:\3:\4:\5:\6\r\n",data)
f.close()

f = open(r"ipmaclist.txt","wb")
f.wirte(m)
f.close()