class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1


        length = len(needle)
        c_sum = 0
        mod = (10**9 +7)

        for i in range(length-1, -1, -1):
            c_sum += ((ord(needle[i]) - ord('a') + 1) * 10**(length - i -1 )) 

        c_sum %= mod

        cur = 0
        l, r = 0, 0

        while r < len(needle):
            cur += ((ord(haystack[r]) - ord('a') + 1) * 10**(length - r - 1 ))
            r += 1
        
        cur %= mod

        if c_sum == cur:
            return 0


        while r < len(haystack):
            ch_l = ord(haystack[l]) - ord('a') + 1
            ch_r = ord(haystack[r]) - ord('a') + 1
            cur = ((cur - (ch_l* 10**(length-1)))* 10) + ch_r
            l += 1
            r += 1

            cur %= mod

            if cur == c_sum:
                return l
        
        return -1

        

        