# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def rev(node):
    prev = None
    while True:
        temp = node.next
        node.next = prev
        prev = node
        if temp is None:
            return node
        node = temp

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = rev(l1)
        l2 = rev(l2)
        a=0
        b=0
        head = ListNode()
        curr = head
        while(l1!=None or l2!=None):
            if(l1!=None and l2!=None):
                a = (l1.val+l2.val+b)%10
                b = (l1.val+l2.val+b)//10
                l1 = l1.next
                l2 = l2.next
            elif(l1!=None):
                a = (l1.val+b)%10
                b = (l1.val+b)//10
                l1 = l1.next
            elif(l2!=None):
                a = (l2.val+b)%10
                b = (l2.val+b)//10
                l2 = l2.next
            curr.val = a
            if(l1==None and l2==None):
                if(b>0):
                    curr.next = ListNode(b)
            else:
                curr.next=ListNode()
                curr=curr.next
        return rev(head)