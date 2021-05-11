num=int(input())
ec=0
oc=0
t=0
while num:
    r=num%10
    num=num//10
    t=r
    if(t%2==0):
        ec+=1
    elif(t%2!=0):
        oc+=1
if(ec%2==0 and oc%2!=0):
    print("even odd")
elif(ec%2!=0 and oc%2!=0):
    print("odd")
elif(ec%2==0 and oc%2==0):
    print("even")
else:
    print("mixed")
        
    

