class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0 
        n = len(height)
        for i in range(1,n): 
            curr = height[i]
            left = height[i]
            right = height[i]

            for j in range(i): 
                left = max(left, height[j])
            for k in range(i+1,n): 
                right = max(right, height[k])
            count += min(left, right) - curr 
        return count 