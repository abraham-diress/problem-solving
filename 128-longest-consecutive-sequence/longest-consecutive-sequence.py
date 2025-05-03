class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for num in numSet:

            if (num - 1) not in numSet:
                cur_len = 1
                cur_num = num

                while (cur_num + 1) in numSet: 
                    cur_len += 1
                    cur_num += 1
            
                longest = max(longest, cur_len)
        
        return longest

