class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in range(len(operations)): 
            if operations[i] == 'C':
                res.pop()
            elif operations[i] == '+':
                print(res) 
                s1 = res.pop()
                print(s1)
                s2 = res.pop()
                print(s2)
                result = s1 + s2 
                print(res)
                res.append(s2) 
                res.append(s1)
                res.append(result)
                print(res)
            elif operations[i] == 'D': 
                s = res.pop()
                result = s * 2 
                res.append(s)
                res.append(result)
            else: 
                res.append(int(operations[i]))
        return sum(res)