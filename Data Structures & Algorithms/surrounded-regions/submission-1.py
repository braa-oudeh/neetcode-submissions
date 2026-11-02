class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        seen = set() 
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(r,c): 
            if not (r >= 0 and r < ROWS and c >= 0 and c < COLS and board[r][c] == 'O'):
                return 
            board[r][c] = 'T'
            for dr,dc in directions: 
                dfs(r + dr, c + dc)
        for r in range(ROWS):
            dfs(r,0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS - 1, c)
        for r in range(ROWS):
            for c in range(COLS): 
                if board[r][c] == 'T': 
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        