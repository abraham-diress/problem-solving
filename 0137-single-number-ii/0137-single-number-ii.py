class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0 
        cnt = 0 
        
        for i in range(32):
            curSum = 0 
            for num in nums:
                if num < 0:
                    num = -1 * num
                if num & (1 << i):
                    curSum += 1
                    
            if curSum % 3:
                ans |= (1 << i)
        
        for num in nums:
            if num == ans:
                cnt += 1
        
        if cnt == 1:
            return ans 
        else:
            return ans * -1





                
        
        