class Solution:
    def decodeString(self, s: str) -> str:
        
        def rec(i):
            res = ""
            num = 0
            
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '[':
                    string, end = rec(i + 1)
                    res += num * string
                    i = end
                    num = 0
                elif c == ']':
                    return res, i
                else:
                    res += c
                i += 1
            
            return res, i
        
        return rec(0)[0]
                    
                    
            
            
            
            
            
        


    

