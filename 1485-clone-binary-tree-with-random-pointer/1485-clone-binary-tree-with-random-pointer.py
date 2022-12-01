# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        mp = dict()
        
        def gen(node):
            if node is None:
                return None
            else:
                ret = NodeCopy(node.val, gen(node.left), gen(node.right))
                mp[node] = ret
                return ret
        
        def con(node):
            if node is not None:
                if node.random is not None:
                    mp[node].random = mp[node.random]
                con(node.left)
                con(node.right)
        
        ret = gen(root)
        con(root)
        return ret
                