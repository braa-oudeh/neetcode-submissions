class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        maxCount = 0 

        for elem in sett: 
            count = 1
            if elem - 1 not in sett: #beginning of a sequence 
                curr = elem 
                while curr + 1 in sett: 
                    count += 1
                    curr = curr + 1  
            maxCount = max(maxCount, count)
        return maxCount