class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd, pos = 0, 0, 0
        
        while n:
            if n & 1 and pos % 2 == 0:
                even += 1
            elif n & 1 and pos % 2 == 1:
                odd += 1
            n >>= 1
            pos += 1
        
        return [even, odd]
            
                
                
                
            
        
        