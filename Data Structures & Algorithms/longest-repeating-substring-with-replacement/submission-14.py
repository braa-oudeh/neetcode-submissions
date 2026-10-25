class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxRes = 0 
        l = 0 
        for r in range(len(s)): 
            count[s[r]] = 1 + count.get(s[r],0)
            maxKey = max(count, key = count.get)
            print(maxKey)
            if (r - l) + 1  - count[maxKey] > k:
                print(count[s[l]],s[l])
                count[s[l]] -= 1 
                l += 1 
            maxRes = max(maxRes, (r - l) + 1 )
        return maxRes