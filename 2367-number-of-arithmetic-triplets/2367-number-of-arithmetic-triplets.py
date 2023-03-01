class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        h_map = {}
        cnt = 0
        
        for i, v in enumerate(nums):
            h_map[v] = i
            
        
        for num in nums:
            diff_1 = num + diff 
            if diff_1 in h_map:
                diff_2 = diff_1 + diff
                
                if diff_2 in h_map:
                    cnt += 1
        return cnt 
        
        
        
        