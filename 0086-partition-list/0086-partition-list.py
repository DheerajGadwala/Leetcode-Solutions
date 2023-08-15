# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l, g = ListNode(), ListNode()
        lt, gt = l, g
        while head != None:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                gt.next = head
                gt = gt.next
            head = head.next
        gt.next = None
        lt.next = g.next
        return l.next