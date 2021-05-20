def arstrng(n,c):
      s=0
      while n:
            r=n%10
            n=n//10
            s=s+pow(r,c)
      return s
n=int(input())
t=n
c=0
while t:
      t=t//10
      c=c+1
a=arstrng(n,c)
if n==a:
      print('The given number is armstrong number')
else:
      print('The given number is not a armstrong number')
