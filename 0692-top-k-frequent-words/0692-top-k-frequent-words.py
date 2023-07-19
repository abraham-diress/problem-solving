class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)
        maxHeap = [[-f, v] for v, f in count.items()]
        ans = []
        
        heapq.heapify(maxHeap)
        
        for _ in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
            
        return ans