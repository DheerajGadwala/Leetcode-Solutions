# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def find(node = root):
            if node is None:
                return math.inf
            elif node.val == target:
                return node.val
            elif node.val > target:
                fc = find(node.left)
            else:
                fc = find(node.right)
            if abs(fc - target) < abs(node.val - target):
                return fc
            else:
                return node.val
        
        return find()
                