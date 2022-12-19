"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, node: 'Node') -> 'Node':
            return None if node is None else Node(node.val, [self.cloneTree(i) for i in node.children])
            