class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        memo = {}
        
        def dp(r, c):
            if r == m:
                return c
            elif grid[r][c] == 1 and c+1 < n and grid[r][c+1] == 1:
                if (r+1, c+1) not in memo:
                    memo[(r+1, c+1)] = dp(r+1, c+1)
                return memo[(r+1, c+1)]
            elif grid[r][c] == -1 and 0 <= c-1 and grid[r][c-1] == -1:
                if (r+1, c-1) not in memo:
                    memo[(r+1, c-1)] = dp(r+1, c-1)
                return memo[(r+1, c-1)]
            else:
                return -1

        ans = []
        for i in range(n):
            ans.append(dp(0, i))
        
        return ans