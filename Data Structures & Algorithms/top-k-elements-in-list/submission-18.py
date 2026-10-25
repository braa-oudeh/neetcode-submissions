from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            res[num] = 1 + res.get(num,0)
        for number, count in res.items(): 
            buckets[count].append(number)
        sol = []

        for i in range(len(buckets)-1, 0 , -1):
            for j in range(len(buckets[i])):
                sol.append(buckets[i][j])
        return sol[:k]

