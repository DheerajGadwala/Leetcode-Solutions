# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        in1 = self.inOrder(p)
        pr1 = self.preOrder(p)
        in2 = self.inOrder(q)
        pr2 = self.preOrder(q)
        if len(in1) != len(in2):
            return False
        for i in range(len(in1)):
            if(in1[i]!=in2[i]):
                return False
        for i in range(len(pr1)):
            if(pr1[i]!=pr2[i]):
                return False
        return True
    
    def inOrder(self, node):
        if node is None:
            return [None]
        else:
            return self.inOrder(node.left) + [node.val] + self.inOrder(node.right)
        
    def preOrder(self, node):
        if node is None:
            return [None]
        else:
            return [node.val] + self.preOrder(node.left) + self.preOrder(node.right)
    
    