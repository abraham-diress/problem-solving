class Solution:
    def partitionString(self, s: str) -> int:
        _set = set()
        res = 1
        
        for ch in s:
            if ch in _set:
                res += 1
                _set.clear()
            
            _set.add(ch)
        
        return res 
        