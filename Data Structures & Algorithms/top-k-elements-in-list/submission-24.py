class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        data = []
        for num, cnt in counter.items():
            data.append((num,cnt))
        result = sorted(data, key=lambda x: x[1])
        vals = []
        for i in range(len(result)-1,-1,-1): 
            vals.append(result[i][0])
            if len(vals) == k:
                return vals
        