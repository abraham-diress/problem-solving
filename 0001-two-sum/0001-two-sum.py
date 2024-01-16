class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hMap = {}
        
        for i in range(len(nums)):
            
            if nums[i] not in hMap:
                hMap[target - nums[i]] = i
            else:
                return [hMap[nums[i]], i]
        
        

        
        
        
        
    
    
        
        
        