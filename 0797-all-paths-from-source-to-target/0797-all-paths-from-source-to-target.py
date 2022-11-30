class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque()
        res = [] 
        
        q.append([0])
        target = len(graph) - 1
        
        while q:
            curPath = q.pop()
            
            if curPath[-1] == target:
                res.append(curPath)
            
            else:
                neighbors = graph[curPath[-1]]
                for neighbor in neighbors:
                    ls = curPath.copy()
                    ls.append(neighbor)
                    q.append(ls)
        return res
            
            
        
        
        
        