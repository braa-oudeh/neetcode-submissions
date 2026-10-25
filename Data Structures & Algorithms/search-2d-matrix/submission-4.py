class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0]) 

        l,r = 0, ROWS * COLS - 1 

        while l <= r: 
            middle = l + (r - l) // 2 
            mid_value = matrix[middle // COLS][middle % COLS]

            if mid_value == target: 
                return True 
            elif mid_value < target: 
                l = middle + 1 
            else: 
                r = middle - 1 
        return False
