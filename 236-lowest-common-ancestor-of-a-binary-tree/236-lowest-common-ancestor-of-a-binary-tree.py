# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = dict()
        depth = dict()
        def res(node = root, par = None, d = 0):
            if node is not None:
                parent[node] = par
                depth[node] = d
                res(node.left, node, d + 1)
                res(node.right, node, d + 1)
        res()
        
        while p != q:
            if depth[p] > depth[q]:
                p = parent[p]
            elif depth[p] < depth[q]:
                q = parent[q]
            else:
                p = parent[p]
                q = parent[q]
        
        return p
        