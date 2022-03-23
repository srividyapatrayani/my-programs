v=list(map(int,input().split()))
v.sort()
l=len(v)-1
x=l//2+1
y=l//2
p=v[x]+v[y]
#print(p)
q=p/2
#print(q)
if len(v)%2==0:
    print(q)
else:
    print(v[y])
