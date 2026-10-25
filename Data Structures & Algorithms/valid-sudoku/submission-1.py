class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols    = []
        rows    = []
        squares = []

        for c in range(len(board)): 
            col = [board[r][c] for r in range(len(board)) if board[r][c] != '.']
            cols.append(col)
        for r in range(len(board)):
            row = [board[r][c] for c in range(len(board)) if board[r][c] != '.']
            rows.append(row)

        for i in range(0, len(board), 3): 
            for j in range(0, len(board), 3): 
                square = [board[r][c] for r in range(i,i+3) for c in range(j, j+3) if board[r][c] != '.']
                squares.append(square)
        
        
        for i in range(len(board)): 
            if (self.checkListForDuplicates(cols[i]) or self.checkListForDuplicates(rows[i]) or self.checkListForDuplicates(squares[i])):
                return False    # Invalid
        return True 
        
    def checkListForDuplicates(self, num_list: List[str]) -> bool: 
        sett = set()
        for num in num_list: 
            if num in sett: 
                return True 
            else:
                sett.add(num)
        return False
