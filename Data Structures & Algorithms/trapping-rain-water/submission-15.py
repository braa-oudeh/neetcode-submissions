class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        prefix = [0] * n 
        suffix = [0] * n 
        maxLeft = height[0]
        maxRight = height[-1]
        total = 0

        for i in range(1,n): 
            if maxLeft < height[i]: 
                maxLeft = height[i]
            prefix[i] = maxLeft - height[i]
        
        for i in range(n-2,-1,-1): 
            if maxRight < height[i]: 
                maxRight = height[i]
            suffix[i] = maxRight - height[i]

        
        for i in range(n): 
            total += min(suffix[i], prefix[i])
        return total