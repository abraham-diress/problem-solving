class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, math.isqrt(i) + 1):
                 dp[i] = min(dp[i], 1 + dp[i - (j**2)])
                    
        return dp[n]
        
        
                