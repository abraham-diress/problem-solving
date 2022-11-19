class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            
        curr.isEnd = True
        curr.word = word
        
    def dfs(self, node, lst):
        if len(lst) == 3:
            return lst
        if node.isEnd:
            lst.append(node.word)
        
        for child in node.children:
            if child:
                self.dfs(child, lst)
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for product in products:
            self.insert(product)   
        
        curr = self.root
        ans = []
        
        for ch in searchWord:
            idx = ord(ch) - ord('a')
            if curr and curr.children[idx]:
                collections = []
                curr = curr.children[idx]
                self.dfs(curr, collections)
                ans.append(collections)
                
            else:
                ans.append([])
                curr = None
        return ans 
                    
        
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
        self.word = ''
        
    
        