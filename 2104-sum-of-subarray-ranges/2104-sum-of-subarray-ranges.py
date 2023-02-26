class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, answer = len(nums), 0
        stack = []
        
        for right in range(n + 1):
            while stack and (right == n or nums[right] <= nums[stack[-1]]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (right - mid) * (mid - left)
            stack.append(right)
            
        stack.clear()
        for right in range(n + 1):
            while stack and (right == n or nums[right] >= nums[stack[-1]]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (right - mid) * (mid - left)
            stack.append(right)
            
        return answer
        
        