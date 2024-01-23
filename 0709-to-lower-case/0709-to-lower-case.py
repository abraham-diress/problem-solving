class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for char in s:
            if 'A' <= char <= 'Z':  
                res += chr(ord(char) + ord('a') - ord('A'))  
            else:
                res += char
        
        return res
        