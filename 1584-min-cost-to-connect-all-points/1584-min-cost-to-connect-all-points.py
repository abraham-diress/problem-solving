class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    
        minHeap = []
        n = len(points)
        visited = [ False for _ in range(n) ]
        visited[0] = True
        
        first_x, first_y = points[0] 
        
        for i in range(1, n):
            second_x, second_y = points[i]
            cost = abs(first_x - second_x) + abs(first_y - second_y)
            minHeap.append((cost, 0, i))
            
        heapq.heapify(minHeap)
        answer = 0
        count = n - 1
        
        while minHeap and count > 0:
            cost, _from, _to = heapq.heappop(minHeap)
            if visited[_to] == False:
                answer += cost
                count -= 1
                visited[_to] = True
                
                first_x, first_y = points[_to]
                for i in range(n):
                    if not visited[i]:
                        second_x, second_y = points[i]
                        cost = abs(first_x - second_x) + abs(first_y - second_y)
                        heapq.heappush(minHeap, (cost, 0, i))
                        
        return answer
                        
        