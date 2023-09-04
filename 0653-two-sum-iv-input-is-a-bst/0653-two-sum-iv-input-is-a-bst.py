# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []
        def res(node=root):
            nonlocal l
            if node is None:
                return
            else:
                res(node.left)
                l.append(node.val)
                res(node.right)
        
        res()
        i, j = 0, len(l) - 1
        
        while i < j:
            if l[i] + l[j] == k:
                return True
            elif l[i] + l[j] > k:
                j -= 1
            else:
                i += 1
        
        return False