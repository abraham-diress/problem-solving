# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = [] 
        
        def dfs(node, curStr): 
            if not node:
                return 
            
            curStr += str(node.val)
            if not node.left and not node.right:
                ans.append(curStr)
            
            dfs(node.left, curStr + '->')
            dfs(node.right, curStr + '->')
            
        dfs(root, "")
        return ans 
            
            
            
        