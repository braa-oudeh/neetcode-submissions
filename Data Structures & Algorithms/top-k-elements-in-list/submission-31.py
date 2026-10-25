class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count_dict = Counter(nums)
        bucket_arr = [[] for i in range(n)]
        
        for key, val in count_dict.items(): 
            bucket_arr[val-1].append(key) 
        res = []

        for i in range(len(bucket_arr) -1 , -1 , -1): 
            if len(res) < k and bucket_arr[i]:
                for item in bucket_arr[i]:
                    res.append(item)
        return res