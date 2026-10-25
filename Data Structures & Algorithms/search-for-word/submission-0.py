class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word): 
                return True 
            if not self.isValid(r,c,board,i,word,path): 
                return False 
            path.add((r,c))
            res = (dfs(r+1,c,i+1) or 
                    dfs(r-1,c,i+1) or 
                    dfs(r,c+1, i+1) or 
                    dfs(r, c-1, i+1))
            path.remove((r,c))
            return res 

        for r in range(rows):
            for c in range(cols): 
                if dfs(r,c,0): 
                    return True 
        return False            


    def isValid(self,row, col, board,i,word, path): 
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and board[row][col] == word[i] and (row,col) not in path