class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = sub = 0
        for num in nums:
            if num == 0:
                sub += 1
                cnt += sub
            else:
                sub = 0
        return cnt
        