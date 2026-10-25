class Solution:
    def longestPalindrome(self, s: str) -> str:
        currMaxString = ""
        n = len(s)

        dp = [[False] * len(s) for _ in range(len(s))]


        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True 

                    if len(s[i:j+1]) > len(currMaxString): 
                        currMaxString = s[i:j+1]
        return currMaxString 