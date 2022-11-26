# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        lb = dict()
        def res(node = root):
            if node is None:
                return 0
            else:
                dep = 1 + max(res(node.left), res(node.right))
                if dep not in lb:
                    lb[dep] = []
                lb[dep].append(node.val)
                return dep
        res()
        ret = [(d, lb[d]) for d in lb.keys()]
        ret.sort(key = lambda x: x[0])
        ret = [j for i, j in ret]
        return ret