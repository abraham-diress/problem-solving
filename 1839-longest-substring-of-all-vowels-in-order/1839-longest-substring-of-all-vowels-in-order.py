class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        count, ans, l = 1, 0, 0 
        
        for r in range(1, len(word)):
            if word[r-1] < word[r]:
                count += 1
            
            elif word[r-1] > word[r]:
                l = r
                count = 1
            
            if count == 5:
                ans = max(ans, r - l + 1);
        
        return ans
        
        
        
        
        
        
        
#         order_d = {'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o'}
#         i, ans = 1, 0
#         sub_set = set()
#         word = 'u' + word
        
#         for j in range(1, len(word)):
#             if order_d[word[j]] != word[j - 1] and word[j - 1] != word[j]:
#                 i = j
#                 sub_set.clear()
#                 while word[i] != 'a':
#                     i += 1
                
#             # aeeeiiiioooauuuaeiou
#             sub_set.add(word[j])
#             if len(sub_set) == 5 and j < len(word) - 1 and word[j + 1] != word[j]:
#                 ans = max(ans, j - i + 1)
#                 sub_set.clear()
            
#         return ans
                