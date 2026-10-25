class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'(': ')', '[': ']', '{': '}'}

        for elem in s: 
            if elem in hashMap.keys(): 
                stack.append(elem)
            else: 
                if stack and hashMap[stack[-1]] == elem: 
                    stack.pop()
                else:
                    return False
        return len(stack) == 0    
