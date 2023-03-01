class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for i in range(2, n-1):
            temp = ""
            j = n
            while j > 0:
                temp += str(j%i)
                j //= i
            if temp != temp[::-1]: 
                return False
            
        return True
        