class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = [] #[_from, _to, cost]
        n = len(points)
        
        for i in range(n):
            first_x, first_y = points[i]
            
            for j in range(i + 1, n):
                second_x, second_y = points[j]
                cost = abs(first_x - second_x) + abs(first_y - second_y)
                edges.append((i, j, cost))
                
        edges.sort( key = lambda x: x[2])
        obj = DisjointSet(n)
        answer = 0
        count = n - 1
        
        for _from, _to, cost in edges:
            if obj.union(_from, _to):
                answer += cost
                count -= 1
            if count == 0:
                break
                
        return answer
    

class DisjointSet:
    def __init__(self, n):
        self.root = [ i for i in range(n) ]
        self.rank = [0] * n 
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
            
        
        
        
        