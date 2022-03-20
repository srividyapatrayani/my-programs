'''l=[10, 3 , 5, 6, 2]
k=1
p=0
j=[]
for i in range(len(l)+1):
    k=k*l[i]
print(k)'''



l=[int(i) for i in input().split()]
target=int(input())
ll=0
hl=len(l)
for i in range(ll,hl):
    mid=(ll+hl)//2
    if l[mid]==target:
        print("found")
        break
    elif(l[mid]>target):
        ll=mid+1
    elif(l[mid]<target):
        hl=mid-1
        
