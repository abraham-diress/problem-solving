class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ws, w_sum, n= (2*k ) + 1, 0, len(nums)
        ans = [-1] * (n)
        
        if n < ws:
            return ans
        
        for i in range(n):
            w_sum += nums[i] 
            
            if i - ws >= 0:    
                j = i - ws
                w_sum -= nums[j]
            
            if i >= (ws - 1):
                j = i - k
                ans[j] = w_sum // ws
                
        return ans 
        
        
        
        