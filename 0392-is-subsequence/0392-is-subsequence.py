class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        dp = [[-1] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
            
        for i in range(m+1):
            dp[0][i] = 0
            
        for ind1 in range(1, n+1):
            for ind2 in range(1, m+1):
                if s1[ind1-1] == s2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1])
                    
        return dp[n][m]

    def isSubsequence(self, s: str, t: str) -> bool:
        return self.longestCommonSubsequence(s, t) == len(s)