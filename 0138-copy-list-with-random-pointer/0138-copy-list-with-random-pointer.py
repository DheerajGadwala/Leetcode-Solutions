"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = dict()
        rd = dict()
        i = 0
        md = dict()
        curr = head
        while curr is not None:
            d[i] = curr
            rd[curr] = i
            i += 1
            curr = curr.next
        root = Node(0)
        curr = root
        for i in range(len(d)):
            curr.next = Node(d[i].val)
            curr = curr.next
            md[i] = curr
        for i in range(len(d)):
            if d[i].random is not None:
                md[i].random = md[rd[d[i].random]]
        return root.next