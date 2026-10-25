class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr = []
        if len(s) == 1: 
            return s 
        for i in range(len(s)): 
            for j in range(i, len(s)): 
                if self.isPalindrome(s[i:j+1]): 
                    arr.append(s[i:j+1]) 

        return max(arr, key = len)

    def isPalindrome(self,s): 
        return s == s[::-1] 