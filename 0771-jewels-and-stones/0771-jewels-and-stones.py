class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        pattern = f'[{re.escape(jewels)}]'
        
        return len(re.findall(pattern, stones))
        
        