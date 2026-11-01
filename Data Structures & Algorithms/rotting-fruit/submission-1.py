class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time,fresh = 0,0 
        q = deque() 
        ROWS,COLS = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        def searchArea(r,c): 
            nonlocal fresh
            if not (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1):
                return
            q.append([r,c])
            fresh -= 1 
            grid[r][c] = 2 
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    fresh += 1 
                if grid[r][c] == 2: 
                    q.append([r,c])
        
        while q and fresh > 0: 
            for i in range(len(q)): 
                r,c = q.popleft()
                for dr,dc in directions: 
                    searchArea(r + dr, c + dc)
            time += 1 
        return time if fresh == 0 else -1 