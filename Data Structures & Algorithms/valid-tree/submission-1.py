class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge_count= 0 
        preMap = {i: [] for i in range(n)}
        visited = set()
        for u, v in edges: 
            self.addEdge(preMap, u ,v)

        def dfs(i, prev): 
            if i in visited: 
                return False 
            visited.add(i)
            for j in preMap[i]: 
                if j == prev: 
                    continue 
                if dfs(j, i) == False: 
                    return False 
            return True 

        return dfs(0,-1) and len(visited) == n

    def addEdge(self,preMap, u, v): 
        preMap[u].append(v)
        preMap[v].append(u)