class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = {}
        for i in range(len(s)): 
            for j in range(i,len(s)):
                if self.isPalindrome(s[i:j+1]):
                    res[s[i:j+1]] = len(s[i:j+1])
        return max(res, key = res.get)

    def isPalindrome(self,string): 
        return string[::-1] == string