class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        count = 0 
        for num in sett: 
            if num - 1 not in sett: 
                length = 1 
                while (num + length) in sett: 
                    length += 1 
                count = max(count, length)
        return count 
