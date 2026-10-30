class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        n = len(nums)
        # Normal House Robbery    
        dp = [0] * len(nums)
        maxSoFar = 0
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        for i in range(n - 3, -1, -1):
            maxSoFar = max(maxSoFar, dp[i+2])
            dp[i] = nums[i] + maxSoFar

        dp2 = [0] * (len(nums) - 1) 
        maxSoFar2 = 0 
        dp2[-1] = nums[-2]
        dp2[-2] = nums[-3]
        for i in range(n - 4, -1, -1):
            maxSoFar2 = max(maxSoFar2, dp2[i+2])
            dp2[i] = nums[i] + maxSoFar2
        dp[0] = dp2[0]
        return max(dp[0], dp[1], dp[2])