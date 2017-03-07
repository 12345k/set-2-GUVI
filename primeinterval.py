a =int(input())
b =int(input())
flag=0
l=[]
for n in range(a,b+1):
    l.append(n)

for n in l:
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break
        if flag == 0:
            print(n)
            flag = 0
        else:
            flag = 0
    else:
        print(n)

