class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        l, r, curSum, ans, dic = 0, 0, 0, 0, defaultdict(lambda: 0)
        
        while r < len(nums):
            
            dic[nums[r]] += 1
            curSum += nums[r]
            
            while dic[nums[r]] > 1:
                dic[nums[l]] -= 1
                curSum -= nums[l]
                l += 1
            ans = max(ans, curSum)
            r += 1
        
        return ans 
        
        
       