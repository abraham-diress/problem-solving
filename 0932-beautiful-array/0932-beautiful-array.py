class Solution:
    def recurse(self, nums):
        if len(nums) <= 2: return nums
        return self.recurse(nums[::2]) + self.recurse(nums[1::2])
    
    def beautifulArray(self, n: int) -> List[int]:
        return self.recurse([i for i in range(1, n+1)])