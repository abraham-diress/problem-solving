# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        store = {}
        root = descriptions[0][0]
        child = set()
        
        for r, c, isLeft in descriptions:
            if r not in store:
                store[r] = TreeNode(r)
        
            if c not in store:
                store[c] = TreeNode(c)

            if isLeft:
                store[r].left = store[c]
            else:
                store[r].right = store[c]
            
            child.add(c)
            
        
        for r, c, i in descriptions:
            if r not in child:
                root = r
                
        return store[root]
                
        
            
                
                 
                