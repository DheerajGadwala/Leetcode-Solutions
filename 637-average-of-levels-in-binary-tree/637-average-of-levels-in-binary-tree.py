# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        d = defaultdict(list)
        self.lvls(root, 0, d)
        l=[]
        for i in d:
            l.append(sum(d[i])/len(d[i]))
        return l
    
    def lvls(self, node, l, d):
        if node is None:
            pass
        else:
            d[l].append(node.val)
            self.lvls(node.left, l+1, d)
            self.lvls(node.right, l+1, d)