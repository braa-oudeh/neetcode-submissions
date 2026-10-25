class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures): 
            print(index, temperature)
            print(stack)
            while stack and stack[-1][1] < temperature: 
                I,T = stack.pop()
                res[I] = index - I 
            stack.append((index, temperature))
        return res