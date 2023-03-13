class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n 
        ans = [0] * n
        
        if n == 1:
            return [0]
        
        prev = 0
        for i in range(n):
            prev += nums[i]
            prefix[i] = prev
        
        prev = 0
        for i in range(n - 1, -1, -1):
            prev += nums[i]
            postfix[i] = prev
            
        for i in range(n):
            if i == 0:
                ans[i] = postfix[i + 1]
            elif i == (n - 1):
                ans[i] = prefix[i - 1]
            else:
                ans[i] = abs(prefix[i - 1] - postfix[i + 1])
        
        return ans
            
        
        