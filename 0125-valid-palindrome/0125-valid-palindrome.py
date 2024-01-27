class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = [c.lower() for c in s if c.isalnum()]
        
        for c in s:
            if c.isalnum():
                if not stack or c.lower() != stack.pop():
                    return False
        
        return True
