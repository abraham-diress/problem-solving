class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
                
            cur = cur.children[idx]
        
        cur.end = word
    
    def dfs(self, cur_node, cur_list):
        if len(cur_list) == 3:
            return 
        
        if cur_node.end:
            cur_list.append(cur_node.end)
        
        for ch in cur_node.children:
            if ch:
                self.dfs(ch, cur_list)
            
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = [] 
        cur = self.root

        for product in products:
            self.insert(product)
        
         
        for ch in searchWord:              
            idx = ord(ch) - ord('a')
            
            if cur and cur.children[idx]:
                temp = []
                self.dfs(cur.children[idx], temp)
                ans.append(temp)
                cur = cur.children[idx]
                
            else:         
                ans.append([])
                cur = None  
        
        return ans 
        
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = None 