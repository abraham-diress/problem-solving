class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        edges = [(w, _from, _to, i) for i, (_from, _to, w) in enumerate(edges) ]
        edges.sort()
    
        uf1 = UnionFind(n)     
        
        #Find the MST weight
        for (w, a, b, _) in edges:
            uf1.union(a, b, w)
            
        minW = uf1.weight
        
        #We exclude to categorize 
        
        ce = []
        pce = []
        m = len(edges)
        
        for i in range(m):
            uf2 = UnionFind(n)
            for j in range(m):
                if i == j:
                    continue
                    
                w, a, b, _ = edges[j]
                uf2.union(a, b, w)
                
            #if weight is > minWeight or incomplete edges then this is ce

            if uf2.weight > minW or uf2.edgeCount < n - 1:
                ce.append(edges[i][3])

            else:
                #Here the edge might not be included in the MST or it may
                #To check that we force to include all edges and check if 
                #it equals the min weight, if so it's pce else it's not

                uf3 = UnionFind(n)
                w, a, b, _ = edges[i]
                uf3.union(a, b, w)
                for j in range(m):
                    w, a, b, _ = edges[j]
                    uf3.union(a, b, w)
                        
                if uf3.weight == minW:
                    pce.append(edges[i][3])
                    
        return ce, pce        

class UnionFind:
    def __init__(self, n):
        self.root = [ i for i in range(n) ]
        self.rank = [0] * n 
        self.weight = 0 
        self.edgeCount = 0
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
    
    def union(self, x, y, w):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        self.weight += w
        self.edgeCount += 1
        
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
        
        