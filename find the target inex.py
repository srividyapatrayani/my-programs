class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def lowerindex(l,u):
                m=0
                while l<=u:
                    m=l+(u-l)//2
                    if nums[m]<=target:
                        #res1.append(m)
                        l = m+1
                    else:
                        u=m-1
                return l
        def upperindex(l,u):
                m=0
                #res2=[]
                while l<=u:
                    m=l+(u-l)//2
                    if nums[m]>=target:
                        u = m -1
                    else:
                        l = m +1
                return l
        nums.sort()
        l=0
        u=len(nums)-1
        x=lowerindex(l,u)
        y=upperindex(l,u)
        if(y>x):
            return [-1] ;
        li = []
        for i in range(y,x):
            li.append(i)
        return li
    
