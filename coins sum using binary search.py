class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=0
        h=n
        res=0
        while l<=h:
            mid=(l+h)//2 #3
            coins=mid*(mid+1)//2 #6
            if n<coins: #5<6
                h=mid-1 #2
            else:
                res=mid 
                l=mid+1
        return res
        
