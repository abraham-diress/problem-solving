class Solution:
    def countDigits(self, num: int) -> int:
        num_copy = num
        cnt = 0

        while num_copy > 0:
            digit = num_copy % 10  
            num_copy = num_copy // 10  

            if digit != 0 and num % digit == 0:
                cnt += 1

        return cnt