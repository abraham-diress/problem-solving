class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        cnts = [0 for i in range(26)]
        cntt = [0 for i in range(26)]

        for i in range(len(s)):
            cnts[ord(s[i]) - ord('a')] += 1
            cntt[ord(t[i]) - ord('a')] += 1
        
        return cnts == cntt 

      