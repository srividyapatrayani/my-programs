def sumofdigits(s,n):
    if n==0:
        print(s)
        return
    s+=n%10
    sumofdigits(s,n//10)

n=int(input())
s=0
print(sumofdigits(s,n))
