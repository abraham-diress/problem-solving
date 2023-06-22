class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        
        def dp(turn, i, M):
            if i >= len(piles):
                return 0
            
            if (turn, i, M) in memo:
                return memo[(turn, i, M)]
            
            res = 0 if turn else float("inf")
            points = 0 
            
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                
                points += piles[i + X - 1]
                if turn:
                    res = max(res, points + dp(not turn, i + X, max(X, M)))
                else:
                    res = min(res, dp(not turn, i + X, max(X, M)))
            
            memo[(turn, i, M)] = res
            return res 
        
        return dp(True, 0, 1)
        
        
                
        
        
        
        