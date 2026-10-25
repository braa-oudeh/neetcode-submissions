class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(sumSoFar, i): 
            if sumSoFar == target: 
                res.append(path.copy())
                return 
            if sumSoFar > target or i >= len(nums): 
                return 
            path.append(nums[i])
            dfs(sumSoFar + nums[i], i)
            path.pop() 
            dfs(sumSoFar, i + 1)
        dfs(0,0)
        return res