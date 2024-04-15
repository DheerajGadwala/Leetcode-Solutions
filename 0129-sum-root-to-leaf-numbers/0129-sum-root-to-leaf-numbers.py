# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def res(node=root, acc=0):
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                return acc*10+node.val
            else:
                return res(node.left, acc*10+node.val) + res(node.right, acc*10+node.val)
        
        return res()
    
    