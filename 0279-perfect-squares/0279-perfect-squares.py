class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        squares = [0]
        
        for j in range(1, math.isqrt(n) + 1):
            squares.append(j**2)
        
        for i in range(2, n + 1):
            for j in range(1, math.isqrt(i) + 1):
                 dp[i] = min(dp[i], 1 + dp[i - squares[j]])
                    
        return dp[n]
        
        
                