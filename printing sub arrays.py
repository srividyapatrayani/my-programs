#printing sub arrays
import math
l=list(map(int,input().split()))
m=[]
z=[]
res=0
n=int(input())
for i in range(len(l)+1):
    for j in range(i):
        m.append(l[j:i])
        print(m)
        
