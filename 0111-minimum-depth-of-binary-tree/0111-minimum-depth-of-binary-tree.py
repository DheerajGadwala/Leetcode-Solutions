# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            return self.Min(node)
        
    def Min(self, node):
        if node is None:
            return math.inf
        elif node.left is None and node.right is None:
            return 1
        else:
            return min(self.Min(node.left), self.Min(node.right))+1