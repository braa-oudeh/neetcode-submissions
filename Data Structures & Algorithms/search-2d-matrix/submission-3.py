class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0]) 
        for r in range(ROWS):
            if self.binSearch(target,matrix[r][:]):
                return True
        return False


    def binSearch(self, target, arr): 
        l = 0 
        r = len(arr) - 1 
        while l <= r: 
            middle = l + (r - l) // 2  
            if arr[middle] == target:
                return True 
            elif arr[middle] < target: 
                l  = middle + 1 
            else: 
                r = middle - 1
        return False
