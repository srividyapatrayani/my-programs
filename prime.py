import math
class Solution:
    def isPrime (self, N):
        i=2
        n=int(math.sqrt(N))
        if N<=1:
                return 0
        if N>1:
            for i in range(i,n+1):
                if N%i==0:
                    return 0
                    break
            else:
                return 1
