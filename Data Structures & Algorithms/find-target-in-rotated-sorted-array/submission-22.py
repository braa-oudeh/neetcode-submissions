class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum index 
        l,r = 0, len(nums) - 1 
        while l < r:
            m = (l + r) // 2  
            if nums[m] > nums[r]: 
                l = m + 1 
            else:
                r = m 
        pivot = l 
    
        l, r = 0,len(nums) - 1 

        if target >= nums[l] and target > nums[r]:
            r = pivot - 1 
        elif target < nums[l] and target <= nums[r]:
            l = pivot 
        while l <= r: 
            m = (l + r) // 2 
            if nums[m] == target: 
                return m 
            elif nums[m] > target: 
                r = m - 1 
            else: 
                l = m + 1 
        return -1 