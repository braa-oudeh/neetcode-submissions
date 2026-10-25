import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = [0] * len(nums)
        minProd = [0] * len(nums)

        maxProd[0] = nums[0]
        minProd[0] = nums[0]

        for i in range(1, len(nums)): 
            maxProd[i] = max(nums[i], maxProd[i-1] * nums[i], minProd[i-1] * nums[i])
            minProd[i] = min(nums[i], maxProd[i-1] * nums[i], minProd[i-1] * nums[i])
        return max(maxProd)
                