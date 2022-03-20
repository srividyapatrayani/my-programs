class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerindex(l,u):
            m=0
            while l<=u:
                m=l+(u-l)//2
                if nums[m]>=target:
                    u=m-1
                else:
                    l=m+1
            return l
        def upperindex(l,u):
            m=0
            while l<=u:
                m=l+(u-l)//2
                if nums[m]<=target:
                    l=m+1
                else:
                    u=m-1
            return u
        nums.sort()
        l=0
        x=0
        y=0
        u=len(nums)-1
        if target in nums:
            x=lowerindex(l,u)
            y=upperindex(l,u)
        else:
            return [-1,-1]
        res=[]
        res.append(x)
        res.append(y)
        return res
