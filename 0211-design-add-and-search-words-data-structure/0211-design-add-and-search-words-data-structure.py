class WordDictionary:

    def __init__(self):
        self.root = TrieNode() 
        self.max_length = 0
    def addWord(self, word: str) -> None:
        current = self.root 
        
        for ch in word:
            idx = ord(ch) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        
        current.isEnd = True
        self.max_length = max(self.max_length, len(word))

    def search(self, word: str) -> bool:
        if len(word) > self.max_length:
            return False
        def modifiedSearch(i, node):
            if not node:
                return False
            if i == len(word):
                return node.isEnd
            
            if word[i] == ".":
                for child in node.children:
                    if child and modifiedSearch(i + 1, child):
                        return True        
            else:
                idx = ord(word[i]) - ord('a')
                return node.children[idx] and modifiedSearch(i + 1, node.children[idx])    
                    
        return modifiedSearch(0, self.root)
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False