class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = [] 
        i, start, end = 0, 0, 1
        
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            ans.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1
        
        ans.append(newInterval)
        
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        
        return ans 
            
                
            
                
        
        
            
        
        
        