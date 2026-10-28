class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        pivot = self.minIdx(nums)
        result = self.binarySearch(0,pivot -1, nums,target)
        if result != -1: 
            return result 
        return self.binarySearch(pivot, len(nums) -1, nums,target)

    def minIdx(self, nums): 
        l,r = 0,len(nums) - 1
        while l < r: 
            m = (l + r) // 2 
            if nums[m] > nums[r]: 
                l = m + 1 
            else:
                r = m
        return l 

    def binarySearch(self, l, r, nums, target): 
        while l <= r: 
            m = (l + r) // 2
            if nums[m] == target: 
                return m 
            elif nums[m] > target: 
                r = m - 1 
            else: 
                l = m + 1 
        return -1 
