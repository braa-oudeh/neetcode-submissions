class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs: 
            count = []
            for char in string: 
                count.append(ord('a') - ord(char))
            if tuple(sorted(count)) in hashmap:
                hashmap[tuple(sorted(count))].append(string)
            else: 
                hashmap[tuple(sorted(count))] = [string]
        return list(hashmap.values())