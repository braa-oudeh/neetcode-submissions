class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        path = set() 
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        max_area = 0

        def isValid(r, c, grid, path): 
            return (r >= 0 and r < ROWS and 
            c >= 0 and c < COLS 
            and (r,c) not in path and 
            grid[r][c] != 0) 

        def dfs(r,c,directions):
            if not isValid(r,c,grid,path): 
                return 0

            path.add((r,c))
            area = 1 
            for dr, dc in directions: 
                area += dfs(r + dr, c + dc, directions)
            return area
        for r in range(ROWS): 
            for c in range(COLS):
                area = dfs(r,c,directions)
                if area :
                    max_area = max(max_area,area)
        return max_area