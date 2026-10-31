class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set() 
        maxArea = 0 
        ROWS, COLS = len(grid), len(grid[0]) 
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        def dfs(r,c): 
            if not (r >= 0 and r < ROWS and c >=0 and c < COLS):
                return 0
            if grid[r][c] == 0 or (r,c) in seen: 
                return 0
            seen.add((r,c)) 
            area = 1 
            for dr,dc in directions: 
                area += dfs(r + dr, c + dc)
            return area 
            


        for r in range(ROWS): 
            for c in range(COLS): 
                    currResult = dfs(r,c)
                    maxArea = max(maxArea, currResult)
        return maxArea