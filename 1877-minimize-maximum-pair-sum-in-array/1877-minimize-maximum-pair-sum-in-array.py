class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = 0 
        l, r = 0, len(nums) - 1
        nums.sort()
        
        while l < r:
            cur = nums[l] + nums[r]
            ans = max(ans, cur)
            l += 1
            r -= 1
        
        return ans
        
        