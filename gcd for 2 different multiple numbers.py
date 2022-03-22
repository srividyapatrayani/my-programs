n=int(input())

    x,y,z=map(int,input().split())
    while x:
        if x>y:
            x=x%y
        else:
            x,y=y,x
    print(y)
        
