1.安装python的excel模块
openpyxl
C:\Users\Allen>python -m pip install openpyxl

>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> ws = wb.active
>>> type(ws)
<class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> ws.append(["姓名","年龄"])
>>> ws.append(["bob","12"])
>>> wb.save(r"C:\Users\Allen\Desktop\python-day04下午\test.xlsx")

2.安装requests  安装bs4
requests 作用等同于urllib 
bs4 作用用来解析html语句的 他认识所有标签