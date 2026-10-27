class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)

        need = len(s1_map)

        for i in range(len(s2)): 
            count2, curr = {}, 0 
            for j in range(i, len(s2)):
                
                count2[s2[j]] = 1 + count2.get(s2[j], 0) 

                if s1_map.get(s2[j], 0) < count2.get(s2[j]): 
                    break 
                
                if s1_map.get(s2[j], 0) == count2[s2[j]]: 
                    curr += 1 
                if curr == need: 
                    return True 
        return False 

