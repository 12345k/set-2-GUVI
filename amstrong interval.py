a = int(input())
b = int(input())
l=[]
count=0
for i in range(a,b+1):
    d=str(i)
    for j in d:
        l.append(j)
    for k in l:
        count = count + int(k)*int(k)*int(k)
    if(count==i):
        print(i,end='')
    l.clear()
    count=0