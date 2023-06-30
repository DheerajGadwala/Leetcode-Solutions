# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if root is None:
            return 0
        
        def res(node = root):
            nonlocal ans
            ret = True
            if node.left is not None:
                l = res(node.left) and node.val == node.left.val
                ret &= l
            if node.right is not None:
                r = res(node.right) and node.val == node.right.val
                ret &= r
            ans += 1 if ret else 0
            return ret
        
        res()
        return ans