# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def res(node):
            nonlocal lca
            if node is None:
                return None
            l = res(node.left)
            r = res(node.right)
            
            if l in [p, q] and r in [p, q]:
                lca = node
                return None
            elif l in [p, q] and node in [p, q]:
                lca = node
                return None
            elif r in [p, q] and node in [p, q]:
                lca = node
                return None
            elif node in [p, q]:
                return node
            elif l is not None:
                return l
            elif r is not None:
                return r
            else:
                return None
        res(root)
        return lca
            