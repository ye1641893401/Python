anum = int(input("请输入成绩："))

if 0 <= anum < 60:
    print("不及格")
elif 60 <= anum < 70:
    print("良")
elif 70 <= anum < 80:
    print("良好")
elif 80 <= anum < 90:
    print("优")
elif 90 <= anum <= 100:
    print("优秀")
else:
    print("输入的数值有误")



"""要求:
1.如果用户写入的数值不在0-100直接屏幕输出您输入的数值有误
2.继续完成从80到100的 好和 优秀的判断
"""
