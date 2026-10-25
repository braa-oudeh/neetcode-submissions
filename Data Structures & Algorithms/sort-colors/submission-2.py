from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        buckets = [[] for _ in range(len(nums))]
        max_val = max(nums)
        for element in nums:
            normalized = element / (max_val + 1)
            bucket_index = int(len(nums) * normalized)
            buckets[bucket_index].append(element)
        list2 = []

        for bucket in (buckets):
            for i in range(len(bucket)):
                list2.append(bucket[i])
        
        for i in range(len(list2)):
            nums[i] = list2[i]
        
