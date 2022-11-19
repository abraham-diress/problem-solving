class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
            
        current.isEnd = True
        
    def prefixCheck(self, word):    
        cur = self.root
        for ch in word:
            if cur.isEnd:
                return True
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
            
        return cur.isEnd
            
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        answer = []
        folder.sort()
        for f in folder:
            chars = f.split('/')
            if not self.prefixCheck(chars):
                self.insert(chars)
                answer.append(f)
        return answer
        
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
    
        