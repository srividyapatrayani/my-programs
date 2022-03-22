import math

class Solution:
    def gcd(self, n, arr):
        res=arr[0]
        i=1
        for i in range(len(arr)):
            res=math.gcd(res,arr[i])
            
        return res
