# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        cnt = 0
        while curr != None:
            cnt += 1
            curr = curr.next
        
        sizes = [cnt//k for i in range(k)]
        for i in range(cnt % k):
            sizes[i] += 1
        
        curr = head
        ret = []
        for i in sizes:
            ret.append(curr)
            for j in range(i-1):
                curr = curr.next
            if curr is not None:
                temp = curr.next
                curr.next = None
                curr = temp
                
        return ret
                