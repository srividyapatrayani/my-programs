def sol(a):#7
    t=0
    while a!=1:
        print(a,end=" ")
        if a%2==0:
            a=a//2
        else:
            a=(3*a)+1
            
a=int(input())
sol(a)


