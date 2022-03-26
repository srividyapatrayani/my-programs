def missingNumber( A, N):
    A.sort()
    l=[]
    for i in range(1,N+1):
        l.append(i)
    p=list(set(A) - set(l)) + list(set(l) - set(A))
    return(p[-1])
    
