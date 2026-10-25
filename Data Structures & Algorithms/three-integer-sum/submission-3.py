class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i-1]: 
                continue 
            curr = self.twoSum(nums[i+1:], -nums[i])
            if curr: 
                for pair in curr: 
                    res.append([nums[i]] + pair)
        return res
    def twoSum(self, nums, target): 
        res = []
        seen = set()
        l = 0 
        r = len(nums) - 1 

        while l < r: 
            if nums[l] + nums[r] == target and (nums[l],nums[r]) not in seen: 
                res.append([nums[l], nums[r]])
                seen.add((nums[l],nums[r]))
                l += 1 
            elif nums[l] + nums[r] < target: 
                l += 1 
            else: 
                r -= 1 
        return res