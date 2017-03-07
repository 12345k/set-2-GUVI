flag =0
n=int(input())
if n > 2:
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag == 0:
        print("prime number")
    else:
        print("not")
else:
    print("prime number")