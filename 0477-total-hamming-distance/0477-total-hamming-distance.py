class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0 
        
        for i in range(32):
            count1 = 0
            count0 = 0
            
            for num in nums:
                if (1 << i) & num:
                    count1 += 1
                else:
                    count0 += 1
            
            ans += count1 * count0
        
        return ans 
        