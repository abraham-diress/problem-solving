class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int: 
        
        return sorted(nums[:3])[1] if len(nums) > 2 else -1
            
                                                                                              