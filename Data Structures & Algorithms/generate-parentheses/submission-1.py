class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openTag, closingTag,stack): 
            if openTag == closingTag == n: 
                res.append("".join(stack)) 
                return 
            if openTag < n: 
                stack.append('(')
                dfs(openTag+1, closingTag, stack)
                stack.pop()
            if closingTag < openTag:
                stack.append(')')
                dfs(openTag, closingTag+1, stack)
                stack.pop()
        dfs(0,0,[])
        return res