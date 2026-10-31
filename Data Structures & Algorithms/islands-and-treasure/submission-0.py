class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,1], [0,-1]] 
        seen = set()
        q = deque()

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 0: 
                    q.append([r,c])
                    seen.add((r,c))
        def addRoom(r,c): 
            if not (r >= 0 and r < ROWS and c >= 0 and c < COLS and (r,c) not in seen and grid[r][c] != -1): 
                return 
            q.append([r,c])
            seen.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)): 
                r, c= q.popleft() 
                grid[r][c] = dist 
                for dr,dc in directions: 
                    addRoom(r + dr, c + dc)
            dist+=1
