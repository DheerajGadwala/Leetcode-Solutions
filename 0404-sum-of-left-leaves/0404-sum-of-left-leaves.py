# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, node: TreeNode, origin=False) -> int:
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return node.val if origin else 0
        else:
            return self.sumOfLeftLeaves(node.left, True) + self.sumOfLeftLeaves(node.right, False)