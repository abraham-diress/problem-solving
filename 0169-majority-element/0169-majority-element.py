class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        majority, count = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == majority:
                count += 1
            elif count <= 0:
                count += 1
                majority = nums[i]
            else:
                count -= 1
        
        return majority
      