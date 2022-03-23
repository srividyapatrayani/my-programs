def sumsquare(n):
    for i in range(n):
        if i*i==n:
            return(True)
    return(False)
n=int(input())
print(sumsquare(n))
