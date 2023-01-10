# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def res(p = p, q = q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                return p.val == q.val and res(p.left, q.left) and res(p.right, q.right)
    
        return res()
    