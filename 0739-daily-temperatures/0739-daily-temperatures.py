class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] 
        
        for ind, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                    stackVal, stackInd = stack.pop()
                    ans[stackInd] = (ind - stackInd)
              
            stack.append([val, ind])
            
        return ans 
            
            
        
       