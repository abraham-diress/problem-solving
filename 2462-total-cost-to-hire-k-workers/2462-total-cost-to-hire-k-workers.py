class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        minHeap = [] 
        l, r = 0, len(costs) - 1
        ans = 0
        
        while l < candidates:
            heappush(minHeap, (costs[l], l))
            l += 1
        
        while r >= len(costs) - candidates and r >= l:
            heappush(minHeap, (costs[r], r))
            r -= 1
        
        for _ in range(k):
            cost, idx = heappop(minHeap)
            ans += cost
            
            if idx < l and l <= r:
                heappush(minHeap, (costs[l], l))
                l += 1
            else:
                if l <= r:
                    heappush(minHeap, (costs[r], r))
                    r -= 1
                    
        return ans
                    
                
                
                
        