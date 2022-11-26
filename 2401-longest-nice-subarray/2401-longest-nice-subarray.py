class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        count = [ 0 for _ in range(32) ]
        left, answer = 0, 1
        
        for right in range(len(nums)):
            for i in range(32):
                count[i] += (nums[right] >> i) & 1
            
            while not self.nice(count):
                for i in range(32):
                    count[i] -= (nums[left] >> i) & 1
                left += 1
            
            answer = max(answer, right - left + 1)
            
        return answer
            
    def nice(self, count):
        for i in range(len(count)):
            if count[i] > 1:
                return False
            
        return True 
            
        
            
            
                
        
        
    
        
        
        