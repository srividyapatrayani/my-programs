num=int(input())#1234
s=num#s=1234
r=0
i=0
while(num):
    num=num//10#123 12 1
    i=i+1#1 2 3 4
i=v=i-1#
num=s#1234
d=num//(10**v)#1 2 3 4
h=num%10#4 3 2 1
while(num):
    y=num//(10**i)#1 2 3 4
    num=num%(10**i)#234 34 4
    if i==v:
        y=h
    elif i==0:
        y=d
    r=r*10+y
    i-=1
print(r)


