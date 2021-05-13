num=int(input())
s=num
r=0
i=0
while(num):
    num=num//10
    i=i+1
i=v=i-1
num=s
d=num//(10**v)
h=num%10
while(num):
    y=num%10
    num=num//10
    if i==v:
        y=d
    elif i==0:
        y=h
    r=r*10+y
    i-=1
print(r)


