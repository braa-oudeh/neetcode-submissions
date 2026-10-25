class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap: 
            self.hashMap[key] = [(value, timestamp)]
        else: 
            self.hashMap[key].append((value,timestamp))
        print(self.hashMap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap: 
            return ""
        l = 0 
        r = len(self.hashMap[key]) - 1 

        while l <= r: 
            middle = l + (r - l) // 2 
            if self.hashMap[key][middle][1] <= timestamp: 
                l = middle + 1 
            else: 
                r = middle - 1 
        if r < 0: 
            return ""
        return self.hashMap[key][r][0]