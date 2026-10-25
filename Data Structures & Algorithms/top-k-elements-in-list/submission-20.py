class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            if n not in res: 
                res[n] = 1
            else: 
                res[n] += 1 
        
        for number, count in res.items(): 
            buckets[count].append(number)
        res_2 = []
        for i in range(len(buckets) - 1, 0 , -1): 
            for number in buckets[i]: 
                res_2.append(number)
                if len (res_2) == k: 
                    return res_2