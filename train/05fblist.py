alist = [0,1]

for i in range(1,11):
    alist.append(alist[-1]+alist[-2])
print(alist)
