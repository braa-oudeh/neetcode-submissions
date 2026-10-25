class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        maxCounter = 0
        charSet = set()
        for r in range(len(s)): 
            if s[r] not in charSet: 
                charSet.add(s[r])
            else:
                while l <= r and s[r] in charSet: 
                    charSet.remove(s[l])
                    l += 1 
                charSet.add(s[r])
            maxCounter = max(maxCounter, len(charSet))
        return maxCounter
