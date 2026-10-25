class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minLeftRight = [0] * len(height)

        left_max = 0 

        right_max = 0 

        count = 0 
        for i in range(len(height)):  
            left_max = max(left_max,height[i])
            maxLeft[i] = left_max
        print(maxLeft)

        for i in range(len(height) -1 ,-1, -1): 
            right_max = max(right_max,height[i])
            maxRight[i] = right_max
        print(maxRight)

        for i in range(len(maxRight)): 
            minLeftRight[i] = min(maxRight[i], maxLeft[i]) 
        
        print(minLeftRight)
        for i in range(len(height)): 
            count += minLeftRight[i] - height[i]

        return count 