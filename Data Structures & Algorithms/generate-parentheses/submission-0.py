class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s): 
            if n * 2 == len(s): 
                if self.isValid(s):
                    res.append(s) 
                return 
            dfs(s + '(')
            dfs(s + ')')
        dfs("")
        return res

    def isValid(self, s: str) -> bool: 
        open = 0 
        for char in s: 
            if char == '(': 
                open += 1 
            else: 
                open -=1 
            if open < 0: 
                return False
        return open == 0