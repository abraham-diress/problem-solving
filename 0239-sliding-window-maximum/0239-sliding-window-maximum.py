class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        maxHeap = [(-val, idx) for idx, val in enumerate(nums[:k])]
        heapq.heapify(maxHeap)
        ans = [-maxHeap[0][0]] 
        
        for i in range(k, len(nums)):
            while maxHeap[0][1] <= i - k:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-nums[i], i))
            ans.append(-maxHeap[0][0])
        
        return ans 
            
        
        