class TimeMap:
    def __init__(self):
        self.hashMap = {}     
    def set(self, key: str, value: str, timestamp: int) -> None:        
        if key in self.hashMap: 
            self.hashMap[key].append((value,timestamp))
        else: 
            self.hashMap[key] = [(value, timestamp)]
    def get(self, key: str, timestamp: int) -> str:
        for k, v in self.hashMap.items(): 
            if k == key: 
                l = 0 
                r = len(v) - 1 
                res = ""
                while l <= r: 
                    middle = l + (r - l) // 2 
                    if v[middle][1] <= timestamp: 
                        res = v[middle][0]
                        l = middle + 1 
                    else: 
                        r = middle - 1 
                return res
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)