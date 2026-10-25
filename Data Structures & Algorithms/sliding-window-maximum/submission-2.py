class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - (k - 1)): 
            curr_arr = nums[i:k + i]
            max_elem = max(curr_arr) 
            res.append(max_elem)
        return res
        
