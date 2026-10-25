
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            maps = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                maps[index] += 1 
            res[tuple(maps)].append(word)
        return list(res.values())

