# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        mn = 'z'*1000
        def res(node=root, acc=''):
            nonlocal mn
            c = chr(97+node.val)
            if node.left is not None:
                res(node.left, c+acc)
            if node.right is not None:
                res(node.right, c+acc)
            if node.left is None and node.right is None:
                mn = min(mn, c+acc)
        res()
        return mn
            
            