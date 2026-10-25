class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1 
        maximum = float('-inf')
        while l < r: 
            area = abs(l - r) * min(heights[l],heights[r] )
            if heights[l] <= heights[r]: 
                l += 1 
            else: 
                r -= 1 
            maximum = max(maximum, area)
        return maximum