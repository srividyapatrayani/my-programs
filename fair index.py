x=int(input())
m=list(map(int,input().split()))#4 -1 0 3
n=list(map(int,input().split()))#-2 5 0 3
c=0
for i in range(1,x):
    lefta=0
    leftb=0
    righta=0
    rightb=0
    for k in range(0,i):
        lefta+=m[k]
        print("LA",lefta)
        leftb+=n[k]
        print("LB",leftb)
    for j in range(i,x):
        righta+=m[j]
        print("RA",righta)
        rightb+=n[j]
        print("RB",rightb)
    if(lefta==leftb==righta==rightb):
        c+=1
print(c)
    
x=int(input())
a=list(map(int,input().split()))#4 -1 0 3
b=list(map(int,input().split()))#-2 5 0 3
c=0
for i in range(1,x):#(1,4)
    a[i]=a[i-1]+a[i]
    b[i]=b[i-1]+b[i]
    for i in range(1,x):
        la=a[i-1]
        lb=b[i-1]
        ra=a[x-1]-a[i-1]
        rb=b[x-1]-b[i-1]
        if(la==lb==ra==rb):
            c+=1
print(c)
    
