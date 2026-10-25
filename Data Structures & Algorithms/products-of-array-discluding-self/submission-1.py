class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n 
        right = [0] * n 
        res = [0] * n 

        for i in range(1,len(nums)):
            left[0] = 1 
            left[i] = nums[i-1] * left[i - 1]

        right[-1] = 1 
        i = len(nums) - 2 
        while i >= 0: 
            right[i] = right[i+1] * nums[i+1]
            i -= 1 
        
        for i in range(len(res)): 
            res[i] = left[i] * right[i]
        return res