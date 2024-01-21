class Solution:
    def countDigits(self, num: int) -> int:
        
        def getValidDigit(num):
            num_copy = num
            while num_copy > 0:
                digit = num_copy % 10  
                num_copy = num_copy // 10  

                if digit != 0 and num % digit == 0:
                    yield digit
        
        return sum(1 for _ in getValidDigit(num))