class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if i == 0  and j == 0:
                    dp[i][j] = grid[0][0]
                else:
                    left = grid[i][j]
                    if j > 0:
                        left += dp[i][j - 1]
                    else:
                        left += float('inf')
                    up = grid[i][j]
                    if i > 0:
                        up += dp[i - 1][j]
                    else:
                        up += float('inf')
                    dp[i][j] = min(left, up)
                    
        return dp[n - 1][m - 1]
                    
                
    def dp(self, i, j, grid, memo):
        if i < 0 or j < 0:
            return float('inf')
        if i == 0 and j == 0:
            return grid[0][0]
        if (i, j) in memo:
            return memo[(i, j)]
        
        left = grid[i][j] + self.dp(i, j - 1, grid, memo) 
        up = grid[i][j]  + self.dp(i - 1, j, grid, memo)
         
        memo[(i, j)] = min(left, up)
        return memo[(i, j)]
        
        