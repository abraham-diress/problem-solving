class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        cnt = 0 
        
        for i in range(32):
            cnt += (xor >> i) & 1
        
        return cnt 
        
        