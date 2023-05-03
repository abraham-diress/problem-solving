class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.score += 1
        
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        res = [] 
        
        for word in words:
            root.addWord(word)
        
        for word in words:
            cur = root
            count = 0
            for c in word:
                count += cur.children[c].score
                cur = cur.children[c]
            res.append(count)
        return res
        
        