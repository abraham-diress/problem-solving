class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        lh = len(haystack)
        
        for i in range(lh):
            if (i + ln - 1) < lh and haystack[i: i + ln] == needle:
                return i

        return -1 
        

        