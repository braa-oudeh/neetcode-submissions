class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []
        n = len(heights)
        for i,h in enumerate(heights):
            start = i 
            while stack and stack[-1][-1] > h: 
                idx,height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx 
            stack.append((start, h))
        print(stack)
        for index, height in stack: 
            distance = n - index 
            maxArea = max(maxArea, height * (distance))
        return maxArea