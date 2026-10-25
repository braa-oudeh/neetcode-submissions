class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        res = 0 
        l = 0 
        
        maxFreq = 0
        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r],0)
            maxFreq = max(maxFreq, hashMap[s[r]])
            while (r - l + 1) - maxFreq > k: 
                hashMap[s[l]] -= 1 
                l += 1 
            res = max(res, (r - l) + 1) 
        return res 