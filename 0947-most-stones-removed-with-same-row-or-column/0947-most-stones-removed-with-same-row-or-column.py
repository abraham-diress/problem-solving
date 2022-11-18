class UnionFind:
    def __init__(self, stones):
        self.parent = {}
        self.rank = defaultdict(lambda: 0)
        
        for stone in stones:
            row = - (stone[0] + 1)
            col = stone[1] + 1
            self.parent[row] = row
            self.parent[col] = col
        
        self.count = len(self.parent)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        
        if x_set == y_set:
            return 
        self.count -= 1
        
        if self.rank[x_set] > self.rank[y_set]:
            self.parent[y_set] = x_set 
        elif self.rank[y_set] > self.rank[x_set]:
            self.parent[x_set] = y_set
        else:
            self.parent[y_set] = x_set
            self.rank[x_set] += 1  

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        uf = UnionFind(stones)
        
        for stone in stones:
            row = - (stone[0] + 1)
            col = stone[1] + 1
            uf.union(row, col)
        
        return len(stones) - uf.count
            
            
        
        