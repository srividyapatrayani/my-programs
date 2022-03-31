class Solution:
    import math
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num
        while l<=r:
            mid=(l+r)//2
            if mid**2==num:
                return mid
            if mid**2>num:
                r=mid-1
            if mid**2<num:
                l=mid+1
        return False
