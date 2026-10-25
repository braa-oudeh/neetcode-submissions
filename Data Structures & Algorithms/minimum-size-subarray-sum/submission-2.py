class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res =[]
        l = 0 
        for r in range(len(nums)): 
            while l <= r and sum(nums[l:r + 1]) >= target:
                res.append(nums[l:r+1])
                l+= 1 
        if len(res) == 0:
            return 0
        return self.smallest_length(res)
    def smallest_length(self,arr):
        return min(len(row) for row in arr) 