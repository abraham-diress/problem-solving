class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        
        if endGene not in bank:
            return -1
        
        visit = set()  
        q = deque()
        
        visit.add(startGene)
        q.append((startGene, 0))
        
        while q:
            gene, level = q.popleft()
            if gene == endGene:
                return level
            
            for i in range(len(gene)):
                for letter in 'ACGT':
                    new_gene = gene[:i] + letter + gene[i+1:]
                    if new_gene not in visit and new_gene in bank:
                        q.append((new_gene, level + 1))
                        visit.add(new_gene)
        return -1
            
        
        
        
        
        
        
        
        
        
        
        