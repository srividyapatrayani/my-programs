"""to print a complete list with same values
n=int(input())
prime=["True" for i in range(n+1)]
print(prime)"""
'''def seive(n):
    prime=[True for i in range(n+1)]
    start=2
    while(start*start<=n):
        if(prime[start]==True):
            for i in range(start**2,n+1,start):
                prime[i]=False

        start+=1
    prime[0]=prime[1]=False
    for start in range(n+1):
        if prime[start]:
            print(start,end=" ")'''
#for a list of elements         
'''n=10**6
l=[True]*(n+1)
def fun():
    l[0]=False
    l[1]=False
    for i in range(2,n+1):
        if l[i]==True:
            for j in range(i*i,n+1,i):
                l[i]=False

fun()
print(l)
#seive(n)'''



'''for every single inout seive alfo
def seive(q):
    prime=[True for i in range(q+1)]
    prime[0]=prime[1]=False
    for i in range(2,len(prime)-1):
        if prime[i]==True:
            for j in range(i*i,q+1,i):
                prime[j]==False
    return(prime)
q=int(input())
prime=seive(q)
for i in range(q):
    n=int(input())
    if prime[n]:
        print(True)
    else:
        print(False)'''

    
    
    



            
