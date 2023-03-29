class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        hashSet = set()
        
        for num in nums:
            hashSet.add(num)
            hashSet.add(self.reverse(num))
        
        return len(hashSet)
            
    def reverse(self, num):
        ans = 0
        while num:
            r = num % 10   
            ans = ans * 10 + r
            num = num // 10
            
        return ans
            
            
        
        
        