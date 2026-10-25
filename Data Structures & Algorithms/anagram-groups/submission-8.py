class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs: 
            count = [0] * 26 
            for char in string: 
                count[ord('a') - ord(char)] += 1 
            if tuple(count) in hashmap:
                hashmap[tuple(count)].append(string)
            else:
                hashmap[tuple(count)] = [string]
        return list(hashmap.values())