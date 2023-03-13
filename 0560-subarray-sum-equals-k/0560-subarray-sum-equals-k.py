class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res, prefixSum = 0, defaultdict(lambda: 0)
        curSum = 0
        prefixSum[0] = 1
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            if diff in prefixSum:
                res += prefixSum[diff]
            
            prefixSum[curSum] += 1
                
        return res 
            
                
                
                
            