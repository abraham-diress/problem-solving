class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, l = 0, len(nums)
        while i < l:
            correct = nums[i]
            if nums[i] < l and correct != i:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            
        return l
        
        