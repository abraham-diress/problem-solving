class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for i in range(32):
            curSum = 0
            for num in nums:
                if num < 0:
                    num = -1 * (num) 
                if num & (1 << i):
                    curSum += 1
            if curSum % 3:
                res |= (1 << i)
        
        for num in nums:
            if res == num:
                cnt += 1
        
        if cnt == 1:
            return res
        else:
            return -1*res 






                
        
        