class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = [0] * (right + 1) 
        
        for ls in ranges:
            l, r = ls
            for j in range(l, r + 1):
                if j <= right:
                    ans[j] += 1
        
        for i in range(left, right + 1):
            if ans[i] == 0:
                return False
        
        return True
            
            