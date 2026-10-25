class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0 
        r = (ROWS * COLS) - 1 

        while l <= r: 
            middle = l + (r - l) // 2 
            if matrix[middle // COLS][middle % COLS] == target: 
                return True 
            elif matrix[middle // COLS][middle % COLS] > target: 
                r = middle - 1 
            else: 
                l = middle + 1 

        return False