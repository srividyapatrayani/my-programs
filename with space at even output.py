num,val=map(int,input().split())
for i in range(1,21):
    print(num," X " ,i,"= ", num*i)
    if((num*i)%2==0):
        print(" ")
