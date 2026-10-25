class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i] = tuple(points[i])
        heap = []
        for corrs in points: 
            eucledian_distance = math.sqrt((corrs[0])**2 + (corrs[1])**2)
            heapq.heappush(heap, (eucledian_distance, corrs))
        res = []
        while k != 0: 
            popped_elem = (heapq.heappop(heap))
            res.append(popped_elem[1])
            k -= 1 
        return res