class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2: 
            return min(cost)
        
        dp = [0] * len(cost) 
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(len(cost) -3, -1, -1): 
            dp[i] = cost[i] + min(dp[i+2], dp[i+1])
        return min(dp[0],dp[1])