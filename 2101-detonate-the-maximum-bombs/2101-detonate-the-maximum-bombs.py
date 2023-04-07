class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjList = defaultdict(list)  
        
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(len(bombs)):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    curDis = sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
                    if r1 >= curDis:
                        adjList[i].append(j)
                        
        mx_cnt = 0 
        def dfs(node, visit):
            if node not in adjList:
                return 1 
            
            curDepth = 1
            for child in adjList[node]:
                if child not in visit:
                    visit.add(child)
                    curDepth += dfs(child, visit)     
                
            return curDepth
        
        
        for i in range(len(bombs)):
            visit = set()
            visit.add(i)
            mx_cnt = max(mx_cnt, dfs(i, visit))
            
        return mx_cnt 
        
    
    
            
            
            
            
            
            
                
            
            
                    
        