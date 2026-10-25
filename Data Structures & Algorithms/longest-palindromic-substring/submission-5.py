class Solution:
    def longestPalindrome(self, s: str) -> str:
        currMaxString = ""
        for i in range(len(s)): 
            for j in range(i, len(s)): 
                if self.isPalindrome(s[i:j+1]): 
                    if len(s[i:j+1]) > len(currMaxString): 
                        currMaxString = s[i:j+1]

        return currMaxString

    def isPalindrome(self,s): 
        return s == s[::-1] 