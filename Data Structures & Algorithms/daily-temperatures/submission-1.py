class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures): 
            while stack and stack[-1][0] < temperature: 
                T,I = stack.pop()
                res[I] = index - I 
            stack.append((temperature, index))
        return res