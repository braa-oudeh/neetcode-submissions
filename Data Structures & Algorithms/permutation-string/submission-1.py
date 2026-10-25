class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        res = False 
        for r in range(len(s2)):
            if s2[r] not in s1: 
                l += 1 
            if (r - l) + 1 == len(s1):
                res = self.isPermutation(s1, s2[l:r+1])
                if res == True: 
                    return res
                l += 1 
        return res
    def isPermutation(self,s1: str, s2: str) -> bool: 
        return (Counter(s1) == Counter(s2))