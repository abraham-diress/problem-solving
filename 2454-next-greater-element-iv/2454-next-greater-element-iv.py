class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [-1] * n
        stack = []
        second = []
        for i in range(n):
            while second and nums[i] > nums[second[-1]]:
                curr = second.pop()
                if output[curr] == -1:
                    output[curr] = nums[i]
            temp = []
            while stack and nums[i] > nums[stack[-1]]:
                curr = stack.pop()
                if output[curr] == -1:
                    temp.append(curr)
            stack.append(i)
            second += temp[::-1]
            
        return output
        