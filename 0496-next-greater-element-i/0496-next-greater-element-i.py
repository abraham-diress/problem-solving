class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ref  = {v: i for i, v in enumerate(nums1)} 
        ans = [-1] * len(nums1)
        stack = []
        
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                val = stack.pop()
                ans[ref[val]] = nums2[i]
            if nums2[i] in ref:
                stack.append(nums2[i])  
        return ans 
            
        
            
            
        
        
        
        
        
        