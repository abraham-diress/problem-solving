class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])
        res, last = 0, float('-inf')
        
        for start, end in intervals:
            if start >= last:
                last = end
            else:
                res += 1
                last = min(last, end)
        
        return res