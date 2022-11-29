# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        target = ""
        while head:
            target = target + str(head.val)
            head = head.next


        def dfs(root, path):
            if target in path:
                return True

            if root.left:
                ans =  dfs(root.left, path + str(root.left.val))
                if ans == True:
                    return True

            if root.right:
                ans  = dfs(root.right, path + str(root.right.val))
                if ans == True:
                    return True

            return False

            
        return dfs(root, str(root.val))
        