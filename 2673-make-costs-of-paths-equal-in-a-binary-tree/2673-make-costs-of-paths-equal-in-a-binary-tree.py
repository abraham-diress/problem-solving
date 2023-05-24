class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.ans = 0
        
        def dfs(node):
            if node >= n:
                return 0
            
            left = dfs(node * 2 + 1)
            right = dfs(node * 2 + 2)
            
            if left != right:
                self.ans += abs(right - left)
            
            return cost[node] + max(left, right)
        
        dfs(0)
        return self.ans
        