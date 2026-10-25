class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = (Counter(nums))

        max_value = 0
        max_key = 0

        for keys, values in counter.items(): 
            if max_value < values: 
                max_key = keys
                max_value = values
        return max_key