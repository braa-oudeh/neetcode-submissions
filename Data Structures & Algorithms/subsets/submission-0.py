class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def dfs(i):
            if i == n: 
                res.append(sol[:])
                return
            #Choice 1 dont pick a number 
            dfs(i+1)

            #Choice 2 pick a number 
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
        dfs(0)
        return res