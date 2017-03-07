n=int(input())
count=0
i=1
for i in range(1,13):
    count = i*n
    print(int(n),"*",int(i),"=",int(count))
    count=0