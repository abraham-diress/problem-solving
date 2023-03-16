class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for i in range(n)]
        
        for query in queries:
            r1, c1, r2, c2 = query
            matrix[r1][c1] += 1
            if r2 + 1 < n:
                matrix[r2 + 1][c1] -= 1
            if c2 + 1 < n:
                matrix[r1][c2 + 1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                matrix[r2 + 1][c2 + 1] += 1
        
        for r in range(1, n):
            for c in range(0, n):
                matrix[r][c] += matrix[r - 1][c]
        
        for r in range(n):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c - 1]
        
                
        return matrix
            
            