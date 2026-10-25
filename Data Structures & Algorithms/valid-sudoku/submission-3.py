class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        hashMapRow = defaultdict(list)
        hashMapCol = defaultdict(list)
        hashMapBoxes = defaultdict(list)
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == '.':
                    continue 
                if (board[r][c] in hashMapRow[r] or board[r][c] in hashMapCol[c] or board[r][c] in hashMapBoxes[(r//3,c//3)]):
                    return False 
                hashMapRow[r].append(board[r][c])
                hashMapCol[c].append(board[r][c])
                hashMapBoxes[(r//3,c//3)].append(board[r][c])
            

        return True 