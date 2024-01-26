class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        stack = [char for char in s if char in vowels]

        res = ''
        for char in s:
            if char in vowels:
                res += stack.pop()
            else:
                res += char

        return res