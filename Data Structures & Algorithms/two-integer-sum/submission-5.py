class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, item in enumerate(nums):
            complement = target - item
            if complement in map:
                return [map[complement],index]
            else:
                map[item] = index
        