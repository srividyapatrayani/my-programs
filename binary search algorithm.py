class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid] < target:
                l+=1
            elif(nums[mid]>target):
                h-=1
            else:
                return mid
        return -1
        
