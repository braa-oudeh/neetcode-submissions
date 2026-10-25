class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m 
        COLS = n 
        path = []
        directions = [[-1,0], [0,-1]]

        for i in range(m): 
            path.append([0] * n)
       
        for i in range(m): 
            path[i][0] = 1 
        for i in range(n): 
            path[0][i] = 1 
        
        for r in range(1,ROWS): 
            for c in range(1,COLS): 
                for dr,dc in directions: 
                    path[r][c] += path[r + dr][c + dc]
            
        return path[-1][-1]
