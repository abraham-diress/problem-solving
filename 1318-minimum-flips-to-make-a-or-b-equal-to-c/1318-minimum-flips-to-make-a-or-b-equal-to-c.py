class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        
        for i in range(32):
            a1, b1, c1 = False, False, False 
            
            if a & (1 << i):
                a1 = True
            
            if b & (1 << i):
                b1 = True
            
            if c & (1 << i):
                c1 = True
                                          
            if not c1:
                if a1 and b1:
                    res += 2
                elif a1 or b1:
                    res += 1
            else:
                if not a1 and not b1:
                    res += 1
        
        return res
    
                
                
                
                
                