class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
    
        cur.isEnd += 1
    
    def dfs(self,node,index):
        self.count += node.isEnd
        if not node.children:
            return
        for letter,n in node.children.items():
            for i in range(index,len(self.s)):
                if self.s[i]==letter:
                    self.dfs(n,i+1)
                    break
        return
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = self.root
        
        for word in words:
            self.insert(word)
            
        self.s=s
        self.count=0
        self.dfs(trie, 0)
        return self.count
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = 0
        
        