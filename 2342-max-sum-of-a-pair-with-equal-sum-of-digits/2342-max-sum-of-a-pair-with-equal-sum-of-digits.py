class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hash_map = defaultdict(list)
        ans = -1
        
        for num in nums:
            digit_sum = self.digit_sum(num)
            
            if digit_sum in hash_map:
                ans = max(ans, num - hash_map[digit_sum][0])
            heapq.heappush(hash_map[digit_sum], -num)
                
        return ans 
    
    def digit_sum(self, num):
        sum_digit = 0
        for ch in str(num):
            sum_digit += int(ch)
        
        return sum_digit
    
        
        
        