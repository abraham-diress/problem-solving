# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.dfs(root, 0, targetSum)
    
    def dfs(self, node, curSum, targetSum):
        if not node:
            return 
        
        curSum += node.val
        
        if not node.right and not node.left:
            return curSum == targetSum
        
        return (self.dfs(node.left, curSum, targetSum) or
        self.dfs(node.right, curSum, targetSum))
        
        
        
        
        