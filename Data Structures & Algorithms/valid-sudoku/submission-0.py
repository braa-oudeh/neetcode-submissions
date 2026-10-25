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

        square = [board[i][j] for j in range(3) for i in range(3) if not board[i][j] == "."]
        squares.append(square)

        square = [board[i][j] for j in range(3,6) for i in range(3,6) if not board[i][j] == "."]
        squares.append(square)

        square = [board[i][j] for j in range(6,9) for i in range(6,9) if not board[i][j] == "."]
        squares.append(square)

        square = [board[i][j] for j in range(3) for i in range(3,6) if not board[i][j] == "."]
        squares.append(square)

        square = [board[i][j] for j in range(3) for i in range(6,9) if not board[i][j] == "."]
        squares.append(square)

        square = [board[i][j] for j in range(3,6) for i in range(3) if not board[i][j] == "."]
        squares.append(square)

        square = [board[i][j] for j in range(6,9) for i in range(3) if not board[i][j] == "."]
        squares.append(square)

        square = [board[i][j] for j in range(6,9) for i in range(3,6) if not board[i][j] == "."]
        squares.append(square)

        square = [board[i][j] for j in range(3,6) for i in range(6,9) if not board[i][j] == "."]
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
