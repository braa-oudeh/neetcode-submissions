class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 and word2: 
            return word2 
        elif not word2 and word1: 
            return word1 
        l = 0 
        r = 0 
        string = ""
        while l < len(word1) and r < len(word2): 
            string += word1[l] + word2[r]
            l += 1 
            r += 1 
        if not word1[l:] and word2[r:]: 
            for char in word2[r:]:
                string += char
        elif not word2[r:] and word1[l:]:
            for char in word1[l:]: 
                string += char 
        return string