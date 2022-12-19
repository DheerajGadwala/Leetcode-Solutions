# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        r = None
        hei = None
        def res(node = root, h = 0):
            nonlocal hei, r
            if node is not None:
                res(node.left, h + 1)
                if node is u:
                    hei = h
                elif h == hei and r is None:
                    r = node
                res(node.right, h + 1)
        res()
        return r