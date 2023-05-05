class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        class Trie:
            def __init__(self):
                self.root = dict()
            def insert(self, word):
                c = self.root
                for char in word:
                    if(char not in c):
                        c[char] = dict()
                    c = c[char]
            def find(self, word):
                c = self.root
                i = 0
                n = len(pattern)
                for char in word:
                    if(ord(char) < 97):
                        if(i == n or char != pattern[i]):
                            return False
                        else:
                            i += 1
                            c = c[char]
                    else:
                        if(i < n and char == pattern[i]):
                            i += 1
                        c = c[char]
                return i==n
        t = Trie()
        for word in queries: t.insert(word)
        return [t.find(word) for word in queries]
        