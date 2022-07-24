# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def res(node = root):
            nonlocal ans
            if node is not None:
                l = res(node.left)
                r = res(node.right)
                ret = 1
                if l != 0 and r != 0:
                    if node.left.val == node.val and node.right.val == node.val:
                        ans = max(ans, l + r + 1)
                        return 1 + max(l, r)
                    elif node.left.val == node.val:
                        ans = max(ans, l + 1)
                        return l + 1
                    elif node.right.val == node.val:
                        ans = max(ans, r + 1)
                        return r + 1
                    else:
                        return 1
                elif l != 0 and node.left.val == node.val:
                    ans = max(ans, l + 1)
                    return l + 1
                elif r != 0 and node.right.val == node.val:
                    ans = max(ans, r + 1)
                    return r + 1
                else:
                    return 1
            else:
                return 0
        res()
        return 0 if ans == 0 else ans - 1