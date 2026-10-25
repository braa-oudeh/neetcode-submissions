class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.sort() 
        print(nums1)
        i = 0 
        while i < n: 
            j = 0 
            while j < len(nums1): 
                if nums1[j] == 0: 
                    nums1[j] = nums2[i]
                    break
                j+=1
            i+=1  
        nums1.sort()
        print(nums1)
