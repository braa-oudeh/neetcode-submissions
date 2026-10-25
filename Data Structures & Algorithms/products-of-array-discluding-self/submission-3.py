class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: 
            return

        n = len(nums)
        prefix = [1] * n 
        suffix = [1] * n 
        res = [0] * n

        for i in range(1, len(nums)): 
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1): 
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(res)): 
            res[i] = suffix[i] * prefix[i]
        return res