class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #O(n) space
        stack = [] # [x][0] temp, [x][1] distance

        for i in range(len(temperatures)): 
            while stack and temperatures[i] > stack[-1][0]:
                temp,idx = stack.pop()
                res[idx] = i - idx 
            stack.append([temperatures[i], i])
                
        return res

            