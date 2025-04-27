class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hashMap = {}

        for i in range(len(nums)):
            addend = target - nums[i]
            if addend in hashMap:
                return [hashMap[addend], i]
            hashMap[nums[i]] = i

    
    
        
        
        