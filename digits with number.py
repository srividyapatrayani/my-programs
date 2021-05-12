num=int(input())#12345
ec=0
oc=0
while num:
    r=num%10#4
    num=num//10#123
    #4
    if(r%2==0):
        ec=ec*10+r
    else:#5
        oc=oc*10+r
print(ec,oc)

