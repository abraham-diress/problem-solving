class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [] #Val, Idx
        score = 0 
        
        for i in range(len(nums)):
            heap.append([nums[i], i])
        
        heapify(heap)
        mark = set() 
                        
        while heap:
            val, idx = heappop(heap)
            
            if idx not in mark:
                score += val
                mark.add(idx + 1)
                mark.add(idx - 1)
        
        return score 
        
            
            
            
            
                
            
            
        
        
        
        
        
        
        
        
        
        