num,v1,v2=map(int,input().split())
s=1
v=0#12345 2 3
while num:
    r=num%10
    num=num//10
    if(r%v1==0):
        r=v2
    v=v+r*s
    s=s*10
print(v)



