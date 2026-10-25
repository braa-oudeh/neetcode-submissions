class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        count = len(s)
        if len(s) == len(t):
            for char in t: 
                if char in list_s:
                    list_s.remove(char)
                    count -= 1 
                

        if count == 0:
            return True
        return False
