class Node: 
    def __init__(self, key, value): 
        self.value = value
        self.key = key 
        self.prev = None 
        self.next = None 
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right 
        self.right.prev = self.left 
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])

        new_node = Node(key,value)
        self.insert(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity: 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, key): 
        key.prev.next = key.next 
        key.next.prev = key.prev 

    def insert(self,key):
        tmp = self.right.prev 
        tmp.next = key 
        key.prev = tmp 
        key.next = self.right 
        self.right.prev = key 



