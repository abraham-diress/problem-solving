class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        res = []
        visit = set()
        
        for u, v in adjacentPairs:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        for i in indegree:
            if indegree[i] == 1:
                q.append(i)
                break
        
        while q:
            val = q.popleft()
            
            if val not in visit:
                res.append(val) 
                visit.add(val)
            
                for ch in adjList[val]:
                    q.append(ch)
        
        return res
    
    # {
    #     1: 2,
    #     2: 1, 3,
    #     3: 2, 4
    #     4: 3
    # }
                
                
            
            
        
        