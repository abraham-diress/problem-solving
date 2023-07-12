class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i, ans, curAnd = 0, 0, 0
        
        for j in range(len(nums)):
            
            while (curAnd & nums[j]) != 0:
                curAnd ^= nums[i]
                i += 1
            
            curAnd ^= nums[j]
            ans = max(ans, (j - i + 1))
        
        return ans 
        
        
        
        
        
        
        
                
        
        
    
        
        
        