# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = defaultdict(int)
        self.l(root, 0, level)
        mx = -math.inf
        pos = -1
        for i in level:
            if level[i]>mx:
                mx = level[i]
                pos = i
        return pos+1
        
    def l(self, node, l, levels):
        if node is None:
            pass
        else:
            levels[l] += node.val
            self.l(node.left, l+1, levels)
            self.l(node.right, l+1, levels)