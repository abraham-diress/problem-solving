class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:   
        #Logi: if two numbers have the same modulo over k, their difference is divisible by k 
        d = defaultdict(int)
        prefix = 0
        d[0] = 1
        cnt = 0
        
        for i in range(len(nums)):
            prefix += nums[i]
            cnt += d[prefix % k]     
            d[prefix % k] += 1  
              
        
        return cnt
    
            
    
            
        
        
            
        
        
            
            
        
        
        