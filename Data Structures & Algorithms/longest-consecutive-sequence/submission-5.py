class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        for nums in sett: 
            length = 1 
            if nums - 1 not in sett: 
                while (nums + length) in sett:
                    length += 1 
            res = max(res, length)
        return res