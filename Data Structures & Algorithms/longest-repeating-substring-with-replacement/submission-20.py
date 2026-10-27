class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        maxFreq = 0 
        longestSeq = 0 
        l = 0 

        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
            maxFreq = max(maxFreq, hashMap[s[r]])

            windowSize = (r - l) + 1 

            while ((r -l) + 1) - maxFreq > k: 
                hashMap[s[l]] -= 1 
                maxFreq = hashMap[max(hashMap, key = hashMap.get)]
                l += 1 
            
            longestSeq = max(longestSeq, (r - l) + 1 )
        return longestSeq