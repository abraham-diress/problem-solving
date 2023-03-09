class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        
        parent = self.kthGrammar(n - 1, k // 2 + k % 2)
        isOdd = k % 2 == 1
        
        if parent == 1:
            return 1 if isOdd else 0
        else:
            return 0 if isOdd else 1
        
        
        
        