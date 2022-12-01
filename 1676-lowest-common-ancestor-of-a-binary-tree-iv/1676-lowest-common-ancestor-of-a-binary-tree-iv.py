# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        def res(node = root):
            if node is None:
                return None
            elif node in nodes:
                return node
            else:
                l = res(node.left)
                r = res(node.right)
                if l and r:
                    return node
                elif l:
                    return l
                elif r:
                    return r
                else:
                    return None
        return res()
                
            
            