class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 2:
            return -1 
        else:
            return nums[1]
        