class LRUCache:
    def __init__(self, capacity: int):
        self.lru = []
        self.capacity = capacity
        self.size = 0
    def get(self, key: int) -> int:
        for i in range(len(self.lru)): 
            if self.lru[i][0] == key: 
                tmp = self.lru.pop(i)
                self.lru.append(tmp)
                return tmp[1]
        return -1
    def put(self, key: int, value: int) -> None:
        if not self.lru: 
            self.lru.append([key,value])
            self.size += 1 
        # For updating the value of the key if the key is already there
        for i in range(self.size): 
            if self.lru[i][0] == key: 
                tmp = self.lru.pop(i)
                tmp[1] = value 
                self.lru.append(tmp)
                return 
        # if there are more spaces 
        if self.size < self.capacity: 
            self.lru.append([key,value])
            self.size += 1 
        
        else: 
            self.lru.pop(0)
            self.lru.append([key,value])
        print(self.lru)
