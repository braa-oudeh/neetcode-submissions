class Solution:
    def search(self, nums: Liszt[int], target: int) -> int:
        if not nums: 
            return -1 
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l 
        l,r = 0, len(nums) -1 
        
        if pivot != 0 and target >= nums[0]:
            r = pivot - 1      # left sorted half
        else:
            l = pivot


        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1 
        