class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int: 
        return heapq.nlargest(2, nums)[-1] if len(nums) > 2 else -1
        
            
        