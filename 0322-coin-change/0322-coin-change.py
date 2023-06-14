class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf') for _ in range(amount + 1)]
        
        L = len(memo)
        memo[0] = 0
        
        for i in range(1, L):
            for c in coins:
                
                if c <= i:
                    memo[i] = min(memo[i], 1 + memo[i - c])
        
        if memo[-1] == float('inf'):
            return -1
        return memo[-1]
    