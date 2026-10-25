class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0 
        left = [0] * n
        right = [0] * n 

        for i in range(1,n): 
            left[i] = max(left[i-1], height[i-1])
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1], height[i+1])
        for i in range(n): 
            if height[i] < left[i] and height[i] < right[i]: 
                res += min(left[i], right[i]) - height[i]
        return res