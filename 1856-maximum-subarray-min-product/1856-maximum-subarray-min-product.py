class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = []
        prefix = [0]
        ans = 0
        
        for num in nums:
            prefix.append(prefix[-1] + num)
        
            
        for i, v in enumerate(nums):
            newStart = i
            while stack and v < stack[-1][0]:
                val, idx = stack.pop()
                total = prefix[i] - prefix[idx]
                ans = max(ans, total * val)
                newStart = idx
            stack.append([v, newStart])
        
        for val, start in stack:
            total = prefix[len(nums)] - prefix[start]
            ans = max(ans, total * val)
        
        return ans % (10**9 + 7)
            
        
        
        
        
        