class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Dic = {v: i for i, v in enumerate(nums1)}
        ans = [-1] * len(nums1)
        
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                ans[num1Dic[val]] = nums2[i]
            if nums2[i] in num1Dic:
                stack.append(nums2[i])
            
        return ans