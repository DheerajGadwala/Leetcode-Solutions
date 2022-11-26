# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def sum(node):
            if node is None:
                return 0
            else:
                return node.val + sum(node.left) + sum(node.right)
        return root.val == sum(root.left) + sum(root.right)