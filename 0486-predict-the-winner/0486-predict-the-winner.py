class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def rec(l, r):
            if l == r: 
                return nums[l]
            
            if l > r:
                return 0
            
            choose_l = nums[l] + min(rec(l + 2, r), rec(l + 1, r - 1))
            choose_r = nums[r] + min(rec(l, r - 2), rec(l + 1, r - 1))
            
            return max(choose_l, choose_r)
        
        
        return rec(0, len(nums) - 1) >= sum(nums) / 2