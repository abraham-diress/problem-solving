class Solution:
    def toLowerCase(self, s: str) -> str:
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase = "abcdefghijklmnopqrstuvwxyz"

        mapping = {uppercase[i]: lowercase[i] for i in range(26)}

        res = ""
        for char in s:
            if char in mapping:
                res += mapping[char]
            else:
                res += char

        return res