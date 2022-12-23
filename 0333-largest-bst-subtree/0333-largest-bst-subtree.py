# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        t = None
        largestSize = 0
        
        def res(node = root):
            nonlocal largestSize, t
            ret = None
            if node is None:
                ret = (0, 0, 0)
            elif node.left and node.right:
                l = res(node.left)
                r = res(node.right)
                if l[1] < node.val and node.val < r[0]:
                    ret = (l[0], r[1], l[2] + r[2] + 1)
                else:
                    ret = (math.inf, -math.inf, -math.inf)
            elif node.left:
                l = res(node.left)
                if l[1] < node.val:
                    ret = (l[0], node.val, l[2] + 1)
                else:
                    ret = (math.inf, -math.inf, -math.inf)
            elif node.right:
                r = res(node.right)
                if node.val < r[0]:
                    ret = (node.val, r[1], r[2] + 1)
                else:
                    ret = (math.inf, -math.inf, -math.inf)
            else:
                ret = (node.val, node.val, 1)
            if ret[2] > largestSize:
                largestSize = ret[2]
                t = node
            return ret
        
        res()
        
        return largestSize
                
                
        