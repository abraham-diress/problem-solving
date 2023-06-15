class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = {}
        
        def solve(i):
            if i >= len(nums):
                return True 
            
            if i in dp:
                return dp[i]
            
            if (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                if solve(i + 2):
                    dp[i] = True
                    return dp[i]
                
                if (i + 2) < len(nums) and nums[i + 2] == nums[i + 1]:
                    if solve(i + 3):
                        dp[i] = True
                        return dp[i]
            
            if (i + 2) < len(nums) and nums[i + 1] == nums[i] + 1 and nums[i + 2] == nums[i + 1] + 1:
                if solve(i + 3):
                    dp[i] = True
                    return dp[i] 
            
            dp[i] = False
            return dp[i] 
        
        return solve(0)
        