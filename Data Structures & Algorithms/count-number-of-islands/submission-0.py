class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        ROWS = len(grid)
        COLS = len(grid[0])
        path = set()
        directions = [[-1,0], [1,0], [0, -1], [0, 1]]

        def isValid(r,c,grid,path): 
            return (r >= 0 and r < ROWS 
            and c >= 0 and c < COLS
            and (r,c) not in path 
            and grid[r][c] != '0')
        
        def dfs(sr, sc,directons): 
            if not isValid(sr,sc, grid, path): 
                return 0 
            path.add((sr,sc))
            for dr, dc in directions: 
                dfs(sr + dr, sc + dc, directions)
            return 1 

        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r,c,directions): 
                    count += 1 
        return count 

