# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        def res(n=n):
            if n == 1:
                return [TreeNode(0)]
            else:
                ret = []
                for i in range(1, n - 1):
                    lefts = res(i)
                    rights = res(n - i - 1)
                    for l in lefts:
                        for r in rights:
                            t = TreeNode(0)
                            t.left = l
                            t.right = r
                            ret.append(t)
                return ret
        
        return res()