class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visitSet = set()
        preMap = {i:[] for i in range(numCourses)}
        for u,e in prerequisites: 
            self.addEdge(preMap,u,e)
        
        def dfs(crs): 
            if crs in visitSet: 
                return False
            if preMap[crs] == []: 
                return True 
            visitSet.add(crs)
            for nei in preMap[crs]: 
                if not dfs(nei): 
                    return False 
            visitSet.remove(crs) 
            preMap[crs] = []
            return True 
        for i in range(numCourses): 
            if not dfs(i): 
                return False 
        return True
    def addEdge(self,preMap,u,e): 
        preMap[u].append(e)
    