class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.moiHeap, self.k = nums, k 
        heapq.heapify(self.moiHeap)
        while len(self.moiHeap) > k: 
            heapq.heappop(self.moiHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.moiHeap, val)

        if len(self.moiHeap) > self.k: 
            heapq.heappop(self.moiHeap)
        return self.moiHeap[0]