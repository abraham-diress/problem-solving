class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)

        for i in range(0, n, 2*k):
            j = min(i+k, n)
            s[i:j] = reversed(s[i:j])

        return ''.join(s)

        
        
        