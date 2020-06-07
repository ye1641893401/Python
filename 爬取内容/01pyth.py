urllib模块应用
>>> import urllib.request
>>> response = urllib.request.urlopen("http://10.10.10.215")  #伪装浏览器向服务器发起请求
>>> html = response.read()  #将源码保存入变量
>>> print(html)
b'<html>hello </html>\n'
>>> m = re.search(rb"<html>(.*)</html>\n",html)  #通过正则表达式取值
>>> m.group(1)
b'hello '
>>>
