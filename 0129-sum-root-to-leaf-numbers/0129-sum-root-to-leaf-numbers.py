# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sm = 0
        def inOrder(node, x = 0):
            nonlocal sm
            if node is not None and node.left is None and node.right is None:
                sm += (10 * x + node.val)
            elif node is not None:
                inOrder(node.left, 10 * x + node.val)
                inOrder(node.right, 10 * x + node.val)
        inOrder(root)
        return sm