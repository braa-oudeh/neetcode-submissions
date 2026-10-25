class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        results = nums[-k % len(nums):]
        del nums[-k % len(nums):]
        nums[:] =  results + nums 