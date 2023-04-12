class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        
        for f, t in edges:
            graph[f].append(t)
            
        
        def dfs(node):
            visit.add(node)
            
            for child in graph[node]:
                if child not in visit:
                    dfs(child)
                    
        ans = [[] for _ in range(n)]           
        for i in range(n):
            visit = set()
            dfs(i)
            
            for j in range(n):
                if i != j and j in visit:
                    ans[j].append(i)
                    
        return ans
            
        
        