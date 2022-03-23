class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        #res=[]
        
        
        for i in range(0,len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        #print(o,e)
        res=[1]*(len(e)+len(o))
        x=0
        e.sort()
        for i in e:
            res[x]=i
            x+=2
        #print(res)
        o.sort(reverse=True)
        x=1
        for j in o:
            res[x]=j
            x+=2
        return(res)
            
            
        
                
