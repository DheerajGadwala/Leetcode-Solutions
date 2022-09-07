# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        return self.preOrder(t)
    def preOrder(self, node):
        if node is None:
            return ''
        else:
            ret = str(node.val)
            if node.left is None and node.right is None:
                return ret
            elif node.left is None and node.right is not None:
                return ret + '()(' + self.preOrder(node.right) + ')'
            elif node.left is not None and node.right is None:
                return ret + '('+ self.preOrder(node.left) +')'
            else:
                return ret +'('+ self.preOrder(node.left) +')('+ self.preOrder(node.right)+')'