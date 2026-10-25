class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, nums, seen): 
            if len(path) == len(nums): 
                res.append(path.copy())
                return 
            
            for i in range(len(nums)): 
                if not seen[i]:
                    path.append(nums[i])
                    seen[i] = True 
                    backtrack(path,nums,seen)
                    path.pop()
                    seen[i] = False
        backtrack([], nums, [False] * len(nums))
        return res 
