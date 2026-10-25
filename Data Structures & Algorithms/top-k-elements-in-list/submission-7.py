class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i],0)
        #then we create a list of the keys but sorted by the values
        sorted_arr = sorted(counter.items(), key=lambda item: item[1],reverse = True)
        print(sorted_arr)        
        for i in range(len(sorted_arr)):
            if len(res) != k: 
                res.append(sorted_arr[i][0])
        return res



