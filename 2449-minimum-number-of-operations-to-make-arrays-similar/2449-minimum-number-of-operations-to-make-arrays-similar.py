class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int: 
        # We split the arrays into parity
        # We sort each part
        # We pair the corresponding  values 
        # We calculate the number of operation for each pair
        nums.sort(key = lambda x: [x % 2, x])
        target.sort(key = lambda x: [x % 2, x])
        res = 0
        
        for i in range(len(nums)):
            diff = abs(nums[i] - target[i])
            res += diff // 2
        
        return res // 2
            
        
        
        
        
        
        
        
        
        