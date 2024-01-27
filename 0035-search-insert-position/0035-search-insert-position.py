class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = -1
        hi = len(nums)
        
        while lo + 1 != hi:
            mid = (lo + hi) // 2
            
            if nums[mid] < target:
                lo = mid
            else:
                hi = mid
        
        return hi