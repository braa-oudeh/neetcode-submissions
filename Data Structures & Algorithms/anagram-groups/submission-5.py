from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = {}
        for string in strs: 
            count = [0] * 26 
            for char in string: 
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in mymap.keys(): 
                mymap[tuple(count)] = []
            
            mymap[tuple(count)].append(string)
        print(mymap.keys())
        return list(mymap.values())