class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "": 
            return ""

        counterT = Counter(t)
        have,need = 0, len(counterT)
        res, resLen = [-1,-1], float('infinity')
        l = 0
        window = {}
        for r in range(len(s)): 
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if window[c] == counterT[c] and c in counterT: 
                have += 1 

            while have == need: 
                if (r-l+1) < resLen:
                    resLen = (r - l + 1 ) 
                    res = [l,r]
                
                window[s[l]] -= 1 
                if s[l] in counterT and window[s[l]] < counterT[s[l]]: 
                    have -= 1 
                l += 1 
            
        l ,r = res
        if resLen != float('infinity'): 
            return s[l : r + 1]
        else:
            return ""

        