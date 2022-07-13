# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = dict()
        def preOrder(node, x = 0):
            if node is not None:
                if x not in h:
                    h[x] = [node.val]
                else:
                    h[x].append(node.val)
                preOrder(node.left, x + 1)
                preOrder(node.right, x + 1)
        preOrder(root)
        ret = []
        for i in h:
            ret.append(h[i])
        return ret