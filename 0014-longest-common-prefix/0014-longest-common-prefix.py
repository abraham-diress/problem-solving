class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        
        cur.is_end = True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        cur = self.root
        res = ''
        
        for word in strs:
            self.insert(word)
        
        while cur:
            if len(cur.children) > 1 or cur.is_end:
                return res 
            
            key = list(cur.children)[0]
            res += key
            
            cur = cur.children[key]
        
        return res
            
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
        