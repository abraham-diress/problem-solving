class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> bool:
        res = 0
        
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    res += 1
        
        return res