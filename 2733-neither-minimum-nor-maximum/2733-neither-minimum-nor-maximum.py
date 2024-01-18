class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        _min, _max = min(nums), max(nums)
        
        for num in nums:
            if num != _min and num != _max:
                return num
        
        return -1
            
        