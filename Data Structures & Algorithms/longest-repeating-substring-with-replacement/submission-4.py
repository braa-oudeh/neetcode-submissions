class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        longest = 1
        l = 0 
        for r in range(len(s)): 
            if s[r] not in hashmap: 
                hashmap[s[r]] = 1 
            else: 
                hashmap[s[r]] += 1 
            if not (((r - l) + 1 ) - max(hashmap.values()) <= k):
                hashmap[s[l]] -= 1 
                l += 1 
            longest = max(longest, (r - l) + 1 )
        return longest
        
