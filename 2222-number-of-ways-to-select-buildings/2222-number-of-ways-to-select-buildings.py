class Solution:
    def numberOfWays(self, s: str) -> int:
        right_1, left_1, right_0, left_0 = 0, 0, 0, 0
        ans = 0
        
        for i in range(len(s)):
            right_1 += s[i] == '1'    
            right_0 += s[i] == '0'

        for i in range(len(s)):
            if s[i] == '0':                                             
                left_0 += 1       
                right_0 -= 1      
                ans += (left_1 * right_1)  
            else:
                left_1 += 1     
                right_1 -= 1        
                ans += (left_0 * right_0)       

        return ans 