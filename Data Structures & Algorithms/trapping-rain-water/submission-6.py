class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftBars = [0] * n 
        rightBars = [0] * n
        count = 0
        maxLeftBar = 0
        rightMaxBar = 0 
        for i in range(n):
            maxLeftBar = max(maxLeftBar, height[i])
            leftBars[i] = maxLeftBar
        for i in range(n-1,-1,-1): 
            rightMaxBar = max(rightMaxBar, height[i])
            rightBars[i] = rightMaxBar

        for i in range(n): 
            count += min(leftBars[i], rightBars[i]) - height[i]
        return count 