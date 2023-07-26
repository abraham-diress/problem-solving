class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pair = sorted(pair, key=lambda p: p[1], reverse=True)
        
        minHeap = []
        res = 0
        curSum = 0 
        
        for n1, n2 in pair:
            curSum += n1
            heapq.heappush(minHeap, n1)
            
            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                curSum -= n1Pop
            
            if len(minHeap) == k:
                res = max(res, curSum * n2)
        
        return res
        
        
        