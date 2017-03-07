n = int(input())
d=str(n)
l=[]
count =0
for i in d:
    l.append(i)
for i in l:
    count = count + int(i)*int(i)*int(i)
if(count==n):
    print("amstrong number" )
else:
    print("not")