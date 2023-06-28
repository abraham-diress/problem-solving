class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = {}
        
        def dp(i, j1, j2):
            if (j1 < 0 or j1 >= len(grid[0]) or j2 < 0 or j2 >= len(grid[0])):
                return -1e8
            
            if (i, j1, j2) in memo:
                return memo[(i, j1, j2)]
            
            if i == len(grid) - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
                            
            maxCherries = 0
            for dj1 in range(-1, 2):
                for dj2 in range(-1, 2):
                    value = 0
                    if j1 == j2:
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]
                        
                    value += dp(i + 1, j1 + dj1, j2 + dj2)
                    maxCherries = max(maxCherries, value)
            
            memo[(i, j1, j2)] = maxCherries
            return maxCherries
        
        return dp(0, 0, len(grid[0]) - 1)
    
    
                    
                    
                    
        