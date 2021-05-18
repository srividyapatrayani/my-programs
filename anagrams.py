n=input()
m=input()
d={}
n1=''.join(sorted(n))
m1=''.join(sorted(m))
d[n1]=[]
d[n1].append(n)
if m1 in d.keys():
    print("true")
else:
    print("false")
