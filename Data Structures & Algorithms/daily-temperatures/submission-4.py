class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # this solution requires us to keep track of distance lol 
        stack = [] # position, and temperature 
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures): 
            while stack and temp > stack[-1][-1]: 
                stackP, stackT = stack.pop()
                result[stackP] = i - stackP 
            stack.append((i,temp))
        return result 
