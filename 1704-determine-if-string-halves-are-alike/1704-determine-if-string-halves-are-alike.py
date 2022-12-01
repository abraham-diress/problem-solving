class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt, half = 0, len(s) / 2
        for i, c in enumerate(s):
            if c in "aeiouAEIOU":
                cnt += 1 if i < half else -1 
        return cnt == 0
