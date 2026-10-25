class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"(": ")", '[' : ']', '{' : '}'}
        stack = []

        opening = '([{'
        for i in range(len(s)): 

            if s[i] in opening: 
                stack.append(s[i])
            else:   
                if not stack: 
                    return False
                elem = stack.pop()
                if hashMap[elem] != s[i]: 
                    return False

        return len(stack) == 0