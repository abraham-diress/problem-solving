class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = sum(nums[:k])
        win_avg = win_sum /k 
        
        for j in range(k, len(nums)):
            win_sum += nums[j] 
            win_sum -= nums[j - k]
            win_avg = max(win_avg, win_sum / k)
        
        return win_avg 
            
            
            
            
            
            
        