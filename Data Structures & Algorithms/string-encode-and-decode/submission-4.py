class Solution:
    def encode(self, strs: List[str]) -> str:
        sizes = {}
        encoded_string = ""
        for string in strs: 
            sizes[string] = len(string)
        for string in strs: 
            encoded_string += str(sizes[string]) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s): 
            size = ""
            string = ""
            while s[i] != '#': 
                size += s[i]
                i += 1 
            i += 1 
            j = 0 
            while j < int(size): 
                string += s[i]
                i += 1 
                j += 1 
            res.append(string)
        return res