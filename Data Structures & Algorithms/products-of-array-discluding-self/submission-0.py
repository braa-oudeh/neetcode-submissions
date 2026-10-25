class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1 
        res = [1] * (len(nums))
        for i in range(len(nums)):
            temp = nums[i]
            res[i] = prefix
            prefix *= temp
        
        res2 = [1] * len(nums)
        postfix = 1 
        for i in range(len(res)-1 , -1, -1):
            res2[i] = postfix * res[i]
            postfix *= nums[i]
        return res2
