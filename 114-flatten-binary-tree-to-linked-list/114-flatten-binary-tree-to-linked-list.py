# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        preOrderList = []
        def preOrder(node):
            nonlocal preOrderList
            if node is not None:
                preOrderList.append(node)
                preOrder(node.left)
                preOrder(node.right)
        preOrder(root)
        for i in range(len(preOrderList)-1):
            preOrderList[i].left = None
            preOrderList[i].right = preOrderList[i+1]
        
        