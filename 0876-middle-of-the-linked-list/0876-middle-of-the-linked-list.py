# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a = head
        b = head
        if a.next is None:
            return a
        while(b != None):
            a = a.next
            b = b.next.next
            if b is None:
                break
            if b.next is None:
                break
        return a