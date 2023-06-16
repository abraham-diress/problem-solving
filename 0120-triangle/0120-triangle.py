class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        1. DP data structure
        2. Transition
        3. Base case 
        
        """
        dp = triangle[-1]
        dp.append(0)
        
        for i in triangle[-2::-1]:
            for j, val in enumerate(i):
                dp[j] = val + min(dp[j], dp[j + 1])
        
        return dp[0]
            
            