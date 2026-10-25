class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i: [] for i in range(n)} 
        count = 0 
        visitPath = set()
        for u , v in edges: 
            self.addEdge(preMap, u , v)
        
        def dfs(component): 
            if component in visitPath: 
                return 
            visitPath.add(component)
            for nei in preMap[component]: 
                dfs(nei)
                
        for i in range(n): 
            if i not in visitPath: 
                dfs(i)
                count += 1 
        return count 
    def addEdge(self,preMap ,u, v): 
        preMap[u].append(v)
        preMap[v].append(u)