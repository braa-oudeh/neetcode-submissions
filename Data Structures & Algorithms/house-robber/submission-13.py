class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        maxSoFar = 0
        for i in range(len(nums) - 3, -1, -1):
            maxSoFar = max(maxSoFar, nums[i+2]) 
            nums[i] += maxSoFar
        return max(nums[0], nums[1])