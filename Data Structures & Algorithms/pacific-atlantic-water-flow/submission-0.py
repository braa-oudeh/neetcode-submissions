class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        atl = set()
        pac = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        def isValid(r,c,prevHeight,visit): 
            return (r >= 0 and r < ROWS and
                    c >= 0 and c < COLS and 
                    (r,c) not in visit and 
                    heights[r][c] >= prevHeight)
        def dfs(r,c,visit,prevHeight): 
            if not isValid(r,c, prevHeight, visit): 
                return 
            visit.add((r,c))
            for dr,dc in directions: 
                dfs(r + dr, c + dc, visit, heights[r][c])
            
        for c in range(COLS): 
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS): 
            dfs(r,0,pac,heights[r][0])
            dfs(r, COLS - 1, atl,heights[r][COLS-1])

        
        for r in range(ROWS): 
            for c in range(COLS): 
                if (r,c) in atl and (r,c) in pac: 
                    res.append([r,c])
        return res