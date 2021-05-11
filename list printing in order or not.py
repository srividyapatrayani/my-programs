n=int(input())
data=list(map(int,input().split()))
a=0
d=0    
for i in range(1,n):
      if data[i]>data[i-1]:
          a+=1
      elif data[i]<data[i-1]:
          d+=1
      if(a and d):
            print(False)
            break
else:
    print(True)

      
