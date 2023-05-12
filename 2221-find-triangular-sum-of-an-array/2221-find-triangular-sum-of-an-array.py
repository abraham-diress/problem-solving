class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        return nums[0] if len(nums)==1 else self.triangularSum([(nums[i]+nums[i+1])%10 for i in range(len(nums)-1)])
        