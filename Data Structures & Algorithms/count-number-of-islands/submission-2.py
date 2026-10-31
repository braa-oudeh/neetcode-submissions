class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() 
        res = 0 
        ROWS = len(grid)
        COLS = len(grid[0]) 
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(r,c): 
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return 
            if (r,c) in seen or grid[r][c] == '0':
                return 
            
            seen.add((r,c))
            for dr,dc in directions: 
                dfs(r + dr, c + dc)

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == '1' and (r,c) not in seen:
                    dfs(r,c) 
                    res += 1 
        return res
