# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def tra(node = root):
            nonlocal lca
            if node is not None:
                l = tra(node.left)
                r = tra(node.right)
                if node is p:
                    if l is q or r is q:
                        lca = node
                        return None
                    else:
                        return p
                elif node is q:
                    if l is p or r is p:
                        lca = node
                        return None
                    else:
                        return q
                elif (l is p or r is p) and (l is q or r is q):
                    lca = node
                    return None
                elif l is p or r is p:
                    return p
                elif l is q or r is q:
                    return q
                else:
                    return None
            else:
                return None
        tra()
        return lca