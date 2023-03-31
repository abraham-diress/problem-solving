class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = [] 

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > -self.maxHeap[0]:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
        
        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = heappop(self.maxHeap)
            heappush(self.minHeap, -val)
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -val) 
            
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
    
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()