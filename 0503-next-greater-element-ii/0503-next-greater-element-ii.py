class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
    
        stack = [] #[ind, val]
        res = [-1] * len(nums)
        
        for ind, val in enumerate(nums):
            while stack and val > stack[-1][1]:
                i, el = stack.pop()
                res[i] = val
            stack.append([ind, val])
        
        for ind, val in enumerate(nums):
            while stack and val > stack[-1][1]:
                i, el = stack.pop()
                res[i] = val
        return res
        
            
        
        
        
        
        