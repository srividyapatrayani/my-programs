m=list(map(int,input().split()))
n=list(map(int,input().split()))
res=[1]*(len(m)+len(n))
x=0
for i in m:
    res[x]=i
    x+=2
x=1
for j in n:
    res[x]=j
    x+=2
print(res)
    
