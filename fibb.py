def fibb(n):
    a,b=0,1
    print(a,b,end=" ")
    i=3
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        
        
        











n=int(input())
fibb(n)#function call with one argument
