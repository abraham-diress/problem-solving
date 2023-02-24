class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        
        for num in nums:
            step = 0
            while stack and stack[-1][0] <= num:
                step = max(step, stack.pop()[1])
                
            curStep = 0 
            if stack: 
                curStep = step + 1 
            stack.append([num, curStep])
            ans = max(ans, curStep)
            
        return ans