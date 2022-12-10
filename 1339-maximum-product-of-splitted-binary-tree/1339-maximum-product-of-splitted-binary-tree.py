# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sm = dict()
        def calcPro(node):
            if node is None:
                return 0
            else:
                sm[node] = calcPro(node.left) + node.val + calcPro(node.right)
                return sm[node]
        calcPro(root)
        mx = -math.inf
        def calcMx(node):
            nonlocal mx
            if node is not None:
                if node.left is not None and (sm[root]-sm[node.left]) * sm[node.left] > mx:
                    mx = (sm[root]-sm[node.left]) * sm[node.left]
                if node.right is not None and (sm[root]-sm[node.right]) * sm[node.right] > mx:
                    mx = (sm[root]-sm[node.right]) * sm[node.right]
                calcMx(node.left)
                calcMx(node.right)
        calcMx(root)
        return mx%(10**9+7)
        