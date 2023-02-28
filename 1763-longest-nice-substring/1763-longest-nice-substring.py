class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(len(s)):
                word = s[i:j+1]
                if self.isNice(word) and len(word) > len(ans):
                    ans = word
                    
        return ans
    
    def isNice(self, word):
        cur_word = set(word)
        i = 0

        while i < len(word) and word[i].lower() in cur_word and word[i].upper() in cur_word:
            i += 1

        return True if i == len(word) else False