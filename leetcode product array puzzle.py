class Solution:
    def productExceptSelf(self, nums, n):
        n = len(nums)
        output = [0]*n
        left = 1
        right = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output
