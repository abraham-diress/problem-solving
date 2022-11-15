class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
        self.groupsCount = size
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])   
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return 
        self.groupsCount -= 1
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_x] = root_y
            self.rank[root_y] += 1
        return  

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind(len(accounts))
        email_to_idx = {}
        
        for idx, acc in enumerate(accounts):
            for i in range(1, len(acc)):
                if acc[i] not in email_to_idx:
                    email_to_idx[acc[i]] = idx
                else:
                    union_find.union(idx, email_to_idx[acc[i]])
        
        idx_to_email = defaultdict(list)
        
        for email in email_to_idx:
            idx = email_to_idx[email]
            uP = union_find.find(idx)
            idx_to_email[uP].append(email)
        
        ans = []
        for idx in idx_to_email:
            idx_to_email[idx].sort()
            idx_to_email[idx].insert(0, accounts[idx][0])
            ans.append( idx_to_email[idx])
        
        return ans 
        
        
        
            
                
                
            
                     
        
        
        
        
        
        
         