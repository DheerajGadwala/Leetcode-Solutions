# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def res(node = root):
            if node is None:
                return
            res(node.left)
            res(node.right)
            if node.left and node.right:
                return
            if node.left:
                ret.append(node.left.val)
            if node.right:
                ret.append(node.right.val)
        res()
        return ret