class Solution:
    def floorSqrt(self, x):
        ll=0
        ul=x
        count=1
        if x==1 or x==0:
            return x
        while ll<=ul:
            y=(ll+ul)//2
            sq=y*y
            if sq==x:
                return y
            elif sq>x:
                ul=y-1
            elif sq<x:
                ll=y+1
                count=y
        return count
                
             
             
