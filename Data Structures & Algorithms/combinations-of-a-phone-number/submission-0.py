class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        hashmap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        res = []

        def dfs(i,curr): 
            if i == len(digits): 
                res.append("".join(curr))
                return res
            for char in hashmap[digits[i]]: 
                curr.append(char)
                dfs(i+1, curr)
                curr.pop()
            

        dfs(0,[])    
        return res