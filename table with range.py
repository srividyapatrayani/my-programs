num,val1,val2=map(int,input().split())
for i in range(1,val2+1):
    if((num*i)%val1!=0) and ((num*i)%num==0):
            print(num," X " ,i,"= ", num*i)

        
