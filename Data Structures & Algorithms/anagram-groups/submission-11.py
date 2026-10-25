class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        

        for string in strs:
            freq_arr = [0] * 26  
            for char in string: 
                freq_arr[ord(char) - ord('a')] += 1 
            if tuple(freq_arr) in hashMap: 
                hashMap[tuple(freq_arr)].append(string)
            else: 
                hashMap[tuple(freq_arr)] = [string]
        return list(hashMap.values())