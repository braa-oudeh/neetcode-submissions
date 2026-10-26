class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)

        longestCount = 0

        for num in nums: 
            if (num - 1) not in sett:
                currLength = 1 
                while num + currLength in sett: 
                    currLength += 1 
                longestCount = max(longestCount, currLength)
        return longestCount 