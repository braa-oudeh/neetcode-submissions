class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sett = set(nums)
        arr = []
        for i in range(len(nums)+1): 
            arr.append(i)
        print(arr)

        for num in arr: 
            if num not in sett: 
                return num