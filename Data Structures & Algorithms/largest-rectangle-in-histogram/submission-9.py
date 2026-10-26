class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0 

        for i in range(len(heights)):
            startPos = i
            currNum = heights[i]
            while stack and currNum < stack[-1][0]:
                val, pos = stack.pop()
                startPos = pos 
                maxArea = max(maxArea, val * (i - pos))
            stack.append([currNum, startPos])
        print(stack)
        for i in range(len(stack)):
            maxArea = max(maxArea, stack[i][0] * (len(heights) - stack[i][-1]))
        return maxArea