class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        res = 0
        min_heap = [(0, 0, 0)] 
        
        while min_heap:
            diff, x, y = heappop(min_heap)
            res = max(res, diff)
            
            if x == m-1 and y == n-1:
                return res
            
            if heights[x][y] == 0:
                continue
                
            curr_height = heights[x][y]
            heights[x][y] = 0
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < m and 0 <= new_y < n and heights[new_x][new_y] != 0:
                    new_diff = abs(heights[new_x][new_y] - curr_height)
                    heappush(min_heap, (new_diff, new_x, new_y))
        
        return res