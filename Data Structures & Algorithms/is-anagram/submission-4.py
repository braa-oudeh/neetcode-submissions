class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CountS, CountT = {}, {}
        if len(s) != len(t):
            return False
        for char in range(len(s)): 
            CountS[s[char]] = 1 + CountS.get(s[char],0)
            CountT[t[char]] = 1 + CountT.get(t[char],0)
        for char in CountS:
            if CountS[char] != CountT.get(char,0):
                return False
        return True
        
