class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        h_set = set()
        
        for edge in edges:
            u, v = edge
            adjList[u].append(v)
            adjList[v].append(u)
            h_set.add(u)
            h_set.add(v)
        
        for node in adjList:
            if len(adjList[node]) == len(h_set) - 1:
                return node
            
        
        