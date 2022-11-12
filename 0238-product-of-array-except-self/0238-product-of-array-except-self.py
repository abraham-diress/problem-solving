class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        postfix = [0] * len(nums)
        ans = []
        sum = 1
        
        
        for i in range(len(nums)):
            sum *= nums[i]
            prefix.append(sum)
            
        sum = 1
        j = len(nums) - 1
        for i in reversed(range(len(nums))):
            sum *= nums[j]
            postfix[j] = sum
            j -= 1
        
            
        for i in range(len(nums)):
            if i == 0:
                ans.append(postfix[i+1])
            elif i == len(nums) - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(prefix[i - 1] * postfix[i + 1])
                
        return ans
        