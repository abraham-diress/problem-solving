# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        
        def inorder( node,nums): 
            if node:
                
                inorder( node.left, nums )
                nums.append( node.val )
                inorder( node.right, nums )
                
        def dfs( left, right, nums):
            if left > right:
                return None
            
            else:
                mid = left + ( right - left ) // 2

                root = TreeNode( nums[mid] )

                root.left = dfs( left, mid-1, nums)
                root.right = dfs( mid+1, right, nums)

                return root
        
        inorder( root, nums )
        return dfs( left = 0, right = len(nums)-1, nums = nums)