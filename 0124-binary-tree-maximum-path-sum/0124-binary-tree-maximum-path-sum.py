# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = -math.inf
        def res(node = root):
            nonlocal mx
            ret = -math.inf
            if node.left is None and node.right is None:
                ret = node.val
            elif node.left is None:
                ret = max(node.val, node.val + res(node.right))
            elif node.right is None:
                ret = max(node.val, node.val + res(node.left))
            else:
                l = res(node.left)
                r = res(node.right)
                mx = max(l + r + node.val, mx)
                ret = max(l+node.val, r+node.val, node.val)
            mx = max(mx, ret)
            return ret
        res()
        return mx
                