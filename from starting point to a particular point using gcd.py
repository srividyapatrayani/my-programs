'''import math
n=int(input())
for i in range(n):
    m,n=map(int,input().split())
    if(math.gcd(m,n)==1):
       print("YES")
    else:
        print("NO")'''
import math
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    z=math.gcd(x,y)
    
    m,n=map(int,input().split())
    if(math.gcd(m,n)==z):
        print("YES")
    else:
        print("NO")
