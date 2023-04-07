class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [] 
        
        for num in nums:
            heappush(maxHeap, -(int(num)))
        
        for _ in range(k - 1):
            heappop(maxHeap)
        
        return str(-1*maxHeap[0])
            
            
    