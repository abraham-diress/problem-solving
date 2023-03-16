class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        ans = []
        
        def dfs(node, curPath):
            curPath.append(node)     
            
            if node == n:
                ans.append(curPath.copy())
                return 
            
            for child in graph[node]:
                dfs(child, curPath) 
                curPath.pop()
            
        dfs(0, [])
        return ans
        
        
            
            
            
            
            
            
            
            
            
        
            
        
        
        
        