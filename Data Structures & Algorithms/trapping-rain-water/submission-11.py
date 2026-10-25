class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        maxLeft = height[0]
        maxRight = height[-1]
        rainWater = 0 
        for i in range(1, len(prefix)): 
            if height[i] > maxLeft: 
                maxLeft = height[i]
            prefix[i] = maxLeft - height[i]
        
        for i in range(len(suffix) -2, -1, -1): 
            if height[i] > maxRight: 
                maxRight = height[i]
            suffix[i] = maxRight - height[i]
        for i in range(len(prefix)): 
            rainWater += min(prefix[i], suffix[i])
        return rainWater