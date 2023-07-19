# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        par = dict()
        height = dict()
        def res(node, parent, h = 0):
            if node is not None:
                par[node] = parent
                height[node] = h
                res(node.left, node, h+1)
                res(node.right, node, h+1)
        res(root, None)
        if p not in par or q not in par:
            return None
        while height[p] > height[q]:
            p = par[p]
        while height[q] > height[p]:
            q = par[q]
        while p is not q:
            p = par[p]
            q = par[q]
        return p