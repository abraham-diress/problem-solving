class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prev = pref[0]
        res = [prev] 
        for n in pref[1:]:
            cur = n^prev
            res.append(cur) 
            prev ^= cur 
            
        return res
        