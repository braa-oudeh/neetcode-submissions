class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        

        countT, window = {}, {}
        for char in t: 
            countT[char] = 1 + countT.get(char, 0)
        have, need = 0, len(countT)

        res = [-1,-1]
        resLen = float('infinity')
        l = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and countT[s[r]] == window[s[r]]: 
                have += 1 

            while have == need: 
                if (r - l + 1) < resLen: 
                    res = [l,r]
                    resLen = (r - l) + 1 
                # Shorten the list
                window[s[l]] -= 1 
                # Check that afterwe shorten it, do we still have all the chars? 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1 
                l += 1  


        l,r = res 
        return s[l:r+1] if resLen != float('infinity') else ""