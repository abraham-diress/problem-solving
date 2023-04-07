# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l == r:
                return TreeNode(nums[l])
            if l > r:
                return None
            
            mx = max(nums[l:r+1])
            mx_idx = nums.index(mx)
            
            mx_node = TreeNode(mx)
            
            if mx_idx - 1 >= l:
                mx_node.left = dfs(l, mx_idx - 1)
            if mx_idx + 1 <= r:
                mx_node.right = dfs(mx_idx + 1, r)
            
            return mx_node
        
        return dfs(0, len(nums) - 1)
        