class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        
        q = deque()
        q.append([0, 0])
        visit = set()
        count = 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                
                if (r, c) == (n - 1, n - 1):
                    return count
                
                for dx, dy in dirs:
                    x_new, y_new = dx + r, dy + c
                    
                    if (0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]) and
                       (x_new, y_new) not in visit and grid[x_new][y_new] == 0):
                        visit.add((x_new, y_new))
                        q.append([x_new, y_new])
            count += 1
                        
        return -1 
                    
            
            
        
        
        
        
        
        