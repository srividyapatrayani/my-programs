def convertFive(n):
    l=list(str(n))
    for i in range(len(l)):
        if l[i]=='0':
            l[i]='5'
    return("".join(l))
