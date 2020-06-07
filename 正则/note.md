# 单个字符匹配

. 匹配任意字符

re.findall(r".ood","i asy you good not food") //ood 前别是任意字符

[] 匹配指定的

re.findall(r"[fg]ood","i asy you good not food")

^ 取反

re.findall(r"[^g]ood","i asy you good not food Good")  
<!-- food Good-->

\d 匹配任意数字，与[0-9]同意

re.findall(r"\d","i asy you good not food Good  40") 
[4,0]

re.findall(r"\d\d","i asy you good not food Good  40") 
[40]

\w 匹配[a_z,0-9,_]

re.findall(r"\w","i asy you good? not foo_d G-ood  40") 

\s 匹配空字符串 空格 回车 tab键。。。
re.findall(r"\s","i asy you good not food Good  40") 

# 匹配一组字符

一组字符串匹配
>>> re.findall(r"allen","I am allen allen")
['allen' 'allen']

| 
>>> re.findall(r"allen|tom","I am allen not tom")
['allen','tom']

*匹配前面字符出现0次或多次
>>> re.findall(r"go*gle","I like google not ggle goooogle and gogle")
o出现0 次或多次 * 前的一个字符 是o
[google,goooogle,ggle,gogle]

+ 出现一次或多次
>>> re.findall(r"go+gle","I like google not ggle goooogle and gogle")
[google,goooogle,gogle]

?出现0次或一次
>>> re.findall(r"go?gle","I like google not ggle goooogle and gogle")
[ggle，gogle]

{M,N}至少M最多N
>>> re.findall(r"go{2}gle","I like google not ggle goooogle and gogle")
[google]  <=2

>>> re.findall(r"go{2,6}gle","I like google not ggle goooogle and gogle")

[google,goooogle]    2=< x <= 6

#  特殊符号用法
^ 以XX 开始
>>> re.findall(r"^I","I say Good not food")
[I]

>>> re.findall(r"^I say","I say Good not food")
[I say]

>>> re.findall(r"^say","I say Good not food")
[]   say 不是这一行的开头

$ 以XXX结尾
>>> re.findall(r"say$","I say Good not food")
[]
>>> re.findall(r"food$","I say Good not food")
[food]

单词的边界 画边

>>> re.findall(r"allen","allen.com allen_123 allenWare allen.com")
[allen,allen,allen]

>>> re.findall(r"\ballen\b","allen.com allen_123 allenWare allen.com")
[allen,allen]  _不是边界符 . 空格是

() 分组并保存提取
>>> re.search(r"allen","I am allen")
< re.Match object; span=(5, 10), match='allen'>

>>> re.search(r"allen","I am allenallen")
< re.Match object; span=(5, 10), match='allen'>

>>> re.search(r"allenallen","I am allenallen")
< re.Match object; span=(5, 15), match='allenallen'>
（allen）保存 \1 提取
>>> re.search(r"(allen)\1","I am allenallen")
< re.Match object; span=(5, 15), match='allenallen'>

(allen)\1 === allenallen

sub 匹配关键词 并替换成后面的

以回车 还行结束的 
（\r\n）

贪婪匹配 ？ 

>>> data = "Tom's phone number is:13901234567"
>>> data
"Tom's phone number is:13901234567"
>>> re.findall("\d+",data)
['13901234567']


>>> re.search(".*(\d+)",data)
< re.Match object; span=(0, 33), match="Tom's phone number is:13901234567">
>>> m = re.search(".*(\d+)",data) .*{Tom's phone number is:} (\d+) {13901234567}
<!-- 并没有 贪婪匹配 -->
>>> m.group(1)    ======》  .*{Tom's phone number is:1390123456} (\d+) {7}
'7'
<!-- 解决贪婪匹配 先匹配后面降低前面的优先级 -->
>>> m = re.search(".*?(\d+)",data)
>>> m.group(1)
'13901234567'

