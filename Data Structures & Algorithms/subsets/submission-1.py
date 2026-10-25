class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i,curr): 
            if i == len(nums): 
                res.append(curr.copy())
                return 
            #Skip 
            dfs(i+1, curr)

            # Add 
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
        dfs(0,[])
        return res
