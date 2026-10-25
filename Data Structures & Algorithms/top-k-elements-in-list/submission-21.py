class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can sort them based off the count and grab the top k elements
        # but that would be not optimal
        buckets = [[] for _ in range(0,(len(nums)+1))]
        counter = Counter(nums)
        for num,count in counter.items(): 
            buckets[count].append(num)
        res = []
        for i in range(len(buckets)-1,-1,-1): 
            if buckets[i]: 
                for num in buckets[i]: 
                    res.append(num)
            if len(res) == k:
                break
        return res
