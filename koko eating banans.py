class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(l,r,mid):
            t=0
            for i in range(len(piles)):
                if piles[i]%mid==0:
                    t+=(piles[i]//mid)
                else:
                    t+=((piles[i]//mid)+1)
            return t
        
                    
            
            
        l,r=1,max(piles)
        while l<=r:
            mid=(l+r)//2
            t=time(l,r,mid)
            if t>h:
                l=mid+1
            else:
                  r=mid-1
        return l
        
    
