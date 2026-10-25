class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        sett = set()
        counter = 0 
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c,sett): 
            if not self.isValid(r,c,grid,sett): 
                return 
            sett.add((r,c))
            for dr,dc in directions: 
                dfs(r + dr, c + dc,sett)
        
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == '1' and (r,c) not in sett:
                    dfs(r,c,sett)
                    counter += 1 
        return counter

    def isValid(self, r, c, grid, sett): 
        return (0 <= r < len(grid) and 0 <= c < len(grid[0]) and 
                grid[r][c] == "1" and (r,c) not in sett)