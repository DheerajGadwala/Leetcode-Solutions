# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        
        index = {voyage[i]:i for i in range(len(voyage))}
        ret = []
        notPossible = False
        
        def res(node = root):
            nonlocal notPossible
            if node is not None:
                lc = res(node.left)
                rc = res(node.right)
                if node.left and node.right:
                    p = index[node.val]
                    l = index[node.left.val]
                    r = index[node.right.val]
                    if r == p + 1 and l == p + rc + 1:
                        ret.append(node.val)
                    elif l != p + 1 or r != p + lc + 1:
                        notPossible = True
                elif node.left:
                    p = index[node.val]
                    l = index[node.left.val]
                    if l != p + 1:
                        notPossible = True
                elif node.right:
                    p = index[node.val]
                    r = index[node.right.val]
                    if r != p + 1:
                        notPossible = True
                return lc + rc + 1
            else:
                return 0
        res()
        return [-1] if notPossible else ret
                