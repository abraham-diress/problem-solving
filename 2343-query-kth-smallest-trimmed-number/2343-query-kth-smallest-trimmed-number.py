class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = [] 
        
        for k, trim in queries:
            maxHeap = [] 
            
            for i, num in enumerate(nums):
                heappush(maxHeap, (-1*int(num[-trim:]), -i))
                
                if len(maxHeap) > k:
                    heappop(maxHeap)
                
            ans.append(-1*maxHeap[0][1])
        
        return ans
                    
        