class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() 
        def dfs(total, path, i): 
            if total == target: 
                res.append(path.copy())
                return 
            if total > target or i == len(candidates): 
                return 
            # include canditate 
            path.append(candidates[i])
            dfs(total + candidates[i], path, i + 1)
            path.pop()
            # skip canditate
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 
            dfs(total, path, i+1)
        dfs(0,[],0)
        return res