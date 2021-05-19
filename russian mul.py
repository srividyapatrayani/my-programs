m,n=map(int,input().split())
s=0
while m:
    if m%2!=0:
        s=s+n
    m=m//2
    n=n*2
print(s)
