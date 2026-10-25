class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        limit = 2 * n
        res = []
        path = []

        def dfs(i):
            if i == limit:
                res.append("".join(path))
                return
            path.append("(")
            dfs(i + 1)
            path.pop()
            path.append(")")
            dfs(i + 1)
            path.pop()
        dfs(0)
        new_res = []
        for string in res: 
            if len(string) == limit and self.isValid(string):
                new_res.append(string)
        return new_res

    def isValid(self,arr):
        count = 0
        for c in arr:
            if c == '(':
                count += 1
            else:  
                count -= 1
                if count < 0:  
                    return False
        return count == 0  