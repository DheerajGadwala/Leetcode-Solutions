# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        l = self.inOrder(root)
        x=[]
        for i in range(1, len(l)):
            x.append(abs(l[i]-l[i-1]))
        return min(x)
    def inOrder(self, node):
        if node is None:
            return []
        else:
            return self.inOrder(node.left) + [node.val] + self.inOrder(node.right)