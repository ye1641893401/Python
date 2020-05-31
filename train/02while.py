"1到10的整数和计算"
"1+2+3+4+5+6+7+8+9+10"
anum = 0
count = 0
while count < 10:
    count += 1
    if count % 2:   #奇数为真 偶数为假
        continue
    anum += count    #10以内偶数和计算
print(anum)
    
