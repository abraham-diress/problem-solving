class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)

        pre = 1
        for i in range(len(nums)):    
            prefix[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= post
            post *= nums[i]
        
        return prefix


        


