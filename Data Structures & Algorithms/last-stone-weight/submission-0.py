class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1: 
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            diff = -(x-y)
            if -x > -y: 
                heapq.heappush(stones, -diff)

        return -stones[0] if stones else 0 