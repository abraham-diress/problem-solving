class Solution:
    def minOperations(self, n: int) -> int:
        powsOfTwo = [2**i for i in range(17)]
        
        def calculateMinDiff(n):
            val = float("inf")
            
            for i in range(len(powsOfTwo)):
                k = abs(powsOfTwo[i] - n)
                val = min(k, val)
                
            return val
        
        ans = 0
        while n != 0:
            n = calculateMinDiff(n)
            ans += 1
        return ans
        