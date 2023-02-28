class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        
        for l in range(len(s) - 2):
            win = [s[l], s[l + 1], s[l + 2]]
            unique = set(win)
            
            if len(unique) == 3:
                ans += 1
                
        return ans
            
            
            
            
        