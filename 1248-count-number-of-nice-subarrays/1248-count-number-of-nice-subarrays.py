class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num % 2 for num in nums]
        prefixSum = defaultdict(lambda: 0)
        curSum, answer = 0, 0
        prefixSum[0] = 1
        
        for i in range(len(nums)):
            curSum += nums[i]
            tmp = curSum - k
            
            if tmp in prefixSum:
                answer += prefixSum[tmp]
            
            prefixSum[curSum] += 1
        
        return answer
        
        
        
        
       