class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        def isVowel(ch):
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                return True
            return False
        
        
        prefix = []
        
        for st in words:
            firstCh = st[0]
            secCh = st[-1]
            
            if isVowel(firstCh) and isVowel(secCh):
                prefix.append(1)
            else:
                prefix.append(0)
        
        prev = prefix[0]
        for i in range(1, len(prefix)):
            prefix[i] += prev
            prev = prefix[i]
            

        ans = [0] * len(queries)
        k = 0
        for i, j in queries:
            if i == 0:
                ans[k] = prefix[j] - 0
            else:
                ans[k] = prefix[j] - prefix[i - 1]
            
            k += 1
                
        return ans
            
            
        
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        