class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        ans = 0
        n = len(nums)
        
        for i in range(2 ** n):
            subset = []
            for j in range(n):
                if i >> j & 1:
                    subset.append(nums[j])
            res.append(subset)
        
        max_or = 0
        for num in nums:
            max_or |= num
        
        for sub in res:
            temp = 0
            for el in sub:
                temp |= el
            
            if temp == max_or:
                ans += 1
                
        return ans
        
        
            
        
        
    
        
            
        
        
            
        