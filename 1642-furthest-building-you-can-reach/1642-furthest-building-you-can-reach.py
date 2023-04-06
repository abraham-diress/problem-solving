class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = [] 
        heapq.heapify(maxHeap)
        
        for i in range(len(heights) - 1):
            if heights[i] > heights[i + 1]:
                continue 
            
            bricks -= heights[i + 1] - heights[i]
            heapq.heappush(maxHeap, -(heights[i + 1] - heights[i]))
            
            if bricks < 0:
                bricks += - (heapq.heappop(maxHeap))
                if ladders > 0:
                    ladders -= 1
                else:
                    return i
                
        return len(heights) - 1
        