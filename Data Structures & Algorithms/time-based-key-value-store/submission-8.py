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
                    if v[middle][1] == timestamp: 
                        res = v[middle][0]
                        break
                    elif v[middle][1] > timestamp: 
                        r = middle - 1 
                    else:
                        l = middle + 1 
                        res = v[middle][0]
                return res
        return ""