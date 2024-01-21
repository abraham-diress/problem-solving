class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        for digit in str(num):
            if num % int(digit) == 0:
                cnt += 1
        
        return cnt 