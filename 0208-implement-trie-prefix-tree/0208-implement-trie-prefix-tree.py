class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        
        for ch in word:
            idx = ord(ch) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]          
        current.isEnd = True
        
    def search(self, word: str) -> bool:
        current = self.root
        
        for ch in word:
            idx = ord(ch) - ord('a')
            if current.children[idx]:
                current = current.children[idx]   
            else:
                return False
        
        return current.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if current.children[idx]:
                current = current.children[idx]   
            else:
                return False
        return True
        
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)