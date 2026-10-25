class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sett = set()
        l = 0
        maxLength = 0
        for r in range(len(s)): 
            while s[r] in sett: 
                    sett.remove(s[l])
                    l += 1 
            sett.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength