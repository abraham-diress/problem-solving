class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[-1] = -nums[-1]
        heap = [(-nums[-1], len(nums) - 1)]
        
        for i in range(len(nums) - 2, -1, -1):
            while heap[0][1] > i + k:
                heapq.heappop(heap)
            
            dp[i] = -nums[i] + heap[0][0]
            heapq.heappush(heap, (dp[i], i))
            
        return -dp[0]