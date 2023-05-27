class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxHeap = [] 
        
        stations.append([target, float("inf")])
        
        refuels = 0 
        prev = 0
        
        for location, capacity in stations:
            startFuel -= (location - prev)
            
            while maxHeap and startFuel < 0:
                startFuel += -heapq.heappop(maxHeap)
                refuels += 1
            
            if startFuel < 0:
                return -1
            
            heapq.heappush(maxHeap, -capacity)
            prev = location
        
        return refuels 
            
            
            
            
        