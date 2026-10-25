class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxRes = 0 
        for i in range(len(heights)): 
            smallestBar = heights[i]

            for j in range(i, len(heights)): 
                if heights[j] < smallestBar: 
                    smallestBar = heights[j]
                windowSize = (j - i) + 1 
                rectangleArea = smallestBar * windowSize
                maxRes = max(maxRes, rectangleArea)
        return maxRes