def reverse(data,n):
    r=0
    rn=0
    for i in range(n):
        pn=data[i]
        while(pn):
            r=pn%10
            pn=pn//10
            rn=rn*10+r
        data[i]=rn
        rn=0
n=int(input())
data=list(map(int,input().split()))
reverse(data,n)
for i in data:
    print(i,end=" ")
