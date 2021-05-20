def perfect(n):
      s=0
      i=1
      while i!=n:
            if n%i==0:
                  s=s+i
            i=i+1
      return s
n=int(input())
if perfect(n)==n:
      print("perfect number")
else:
      print("not a perfect number")

