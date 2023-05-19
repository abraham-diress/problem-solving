class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0 
        for num in nums:
            xor ^= num
        
        lsb = 1
        while not xor & lsb:
            lsb <<= 1
        
        div1, div2 = 0, 0 
        for num in nums:
            if num & lsb:
                div1 ^= num
            else:
                div2 ^= num
        
        return [div1, div2]
        
        