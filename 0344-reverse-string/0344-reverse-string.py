class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = list(s)
        
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
        

        
        
        