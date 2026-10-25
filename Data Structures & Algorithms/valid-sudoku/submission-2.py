class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        squareMap = defaultdict(set)
        rowMap = defaultdict(set)
        columnMap = defaultdict(set)

        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rowMap[r]
                    or board[r][c] in columnMap[c]
                    or board[r][c] in squareMap[(r//3,c//3)]):
                    return False
                rowMap[r].add(board[r][c])
                columnMap[c].add(board[r][c])
                squareMap[(r//3,c//3)].add(board[r][c])

        return True


            