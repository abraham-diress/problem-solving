class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curSum, maxFreq = 0, 1

        for right in range(len(nums)):
            curSum += nums[right]
            while (right - left + 1) * nums[right] - curSum > k:
                curSum -= nums[left]
                left += 1
            
            maxFreq = max(maxFreq, (right - left + 1))
        
        return maxFreq









        
        