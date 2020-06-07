 " scrapy"
import urllib.request    

import re

def get_html(url):
    request = urllib.request.Request(url) #准备针对hml进行头部信息上传
    request.add_header("user-agent","Mozilla/5.0 (Windows NT 6.0; Win32; x86)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36") #添加头部信息
    response = urllib.request.urlopen(request)  #发送访问请求
    html = response.read().decode("utf-8")   #获取hml源码
    return html

def get_imghtml(imgpath):
    request = urllib.request.Request(imgpath) #准备针对hml进行头部信息上传
    request.add_header("user-agent","Mozilla/5.0 (Windows NT 6.0; Win32; x86)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36") #添加头部信息
    response = urllib.request.urlopen(request)  #发送访问请求
    imgorg = response.read()
    return imgorg

def get_image(html,url):
    num = 0
    imglist = re.findall(r"style/\w{60}.jpg",html)  #获取不完整的图片地址
    for i in imglist:
        imgpath = url+i   #完善图片地址
        num += 1
        with open(str(num)+".jpg","wb") as f:   #生成图片
            f.write(get_imghtml(imgpath))   

if __name__ == "__main__":
    url = "http://10.10.10.215/"
    html = get_html(url)
    get_image(html,url)
