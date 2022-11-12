class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i = 0 
        j = 0
        
        nums.sort()
        
        win_sum = 0
        freq = 0
        
        for j in range(len(nums)):
            
            win_sum += nums[j]
            
            while ((j - i + 1) * nums[j]) - win_sum > k:
                
                win_sum -= nums[i]
                i += 1
            
            freq = max(freq, (j - i + 1))
        
        return freq