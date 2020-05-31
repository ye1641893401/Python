sf = open(r"C:\Windows\System32\cmd.exe","rb")
df = open(r"c:\users\allen\ncmd.exe","wb")
"为了解决大文件的传输问题 不应该一次读取全部数据 一次4096字节读取"
while True:
    data = sf.read(4096)
    if data == b"":
        break
    df.write(data)

sf.close()
df.close()
