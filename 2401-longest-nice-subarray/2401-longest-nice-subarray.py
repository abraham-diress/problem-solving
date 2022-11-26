class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, answer, total = 0, 0, 0
        
        for right in range(len(nums)):
            
            while total & nums[right] != 0:
                total ^= nums[left]
                left += 1
                
            total ^= nums[right]
            answer = max(answer, right - left + 1)
            
        return answer
     
            
        
            
            
                
        
        
    
        
        
        