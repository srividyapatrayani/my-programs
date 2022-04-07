def counting(s,n):
    if n==0:
        print(s)
        return
    d=n%10
    s+=1
    counting(s,n//10)

n=int(input())
s=0
counting(s,n)
