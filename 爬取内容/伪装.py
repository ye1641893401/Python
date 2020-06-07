为什么要伪装 ，服务器管理员那边可以看到你是用什么浏览器访问的，也就是访问形式
而你被人家看到用python 那么会被禁掉，你用py 肯定不是浏览是 爬取人家信息

>>> url = "http://10.10.10.215"
>>> request = urllib.request.Request(url)
>>> request.add_header("user-agent","Mozilla/5.0 (Windows NT 6.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36")
>>> response = urllib.request.urlopen(request)
>>> html = response.read()

>>> imglist = re.findall(rb"style/\w{60}.jpg",html)

len("style/img/ddddddscnsducsdncusdc.jpg")  查看长度