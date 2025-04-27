class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l, r = 0, 2
        ans = 0

        while r < len(nums):
            if nums[r] + nums[l] == nums[l + 1] / 2:
                ans += 1
            l += 1
            r += 1
        
        return ans
        