class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars_ls = [c.lower() for c in s if c.isalnum()]
        
        return chars_ls == chars_ls[::-1]
