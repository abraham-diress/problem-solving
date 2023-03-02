class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        
        for word in words:
            if word == word[::-1]:
                res= word
                break
                
        return res
        