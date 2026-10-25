class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        hashMapRow = defaultdict(set)
        hashMapCol = defaultdict(set)
        hashMapBoxes = defaultdict(set)
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == '.':
                    continue 
                if (board[r][c] in hashMapRow[r] or board[r][c] in hashMapCol[c] or board[r][c] in hashMapBoxes[(r//3,c//3)]):
                    return False 
                hashMapRow[r].add(board[r][c])
                hashMapCol[c].add(board[r][c])
                hashMapBoxes[(r//3,c//3)].add(board[r][c])
            

        return True 