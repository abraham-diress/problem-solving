class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        
        nums.sort()
        l, r = 0, len(nums) - 1
        boats = 0
        
        while l <= r:
            curSum = nums[l] + nums[r]
            if curSum <= limit:
                l += 1
            r -= 1
            boats += 1
                
        return boats
      
        
        
        