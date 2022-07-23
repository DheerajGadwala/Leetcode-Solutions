# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead = ListNode(-1)
        rightHead = ListNode(-1)
        lc = leftHead
        rc = rightHead
        while head != None:
            if head.val < x:
                lc.next = head
                lc = lc.next
            else:
                rc.next = head
                rc = rc.next
            head = head.next
        lc.next = rightHead.next
        rc.next = None
        return leftHead.next