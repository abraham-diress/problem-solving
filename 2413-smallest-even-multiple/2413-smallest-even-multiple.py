class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if not n % 2:
            return n
        else:
            return n * 2
        
        
        