import heapq

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, h: List[Optional[ListNode]]) -> Optional[ListNode]:
        f = []
        for i in h:
            if i is None:
                continue
            curr = i
            temp = Node(0)
            head = temp
            while curr is not None:
                temp.next = Node(curr.val)
                temp = temp.next
                curr = curr.next
            f.append(head.next)
        heapq.heapify(f)
        head = ListNode(0)
        curr = head
        while len(f) != 0:
            x = heapq.heappop(f)
            curr.next = ListNode(x.val)
            x = x.next
            curr = curr.next
            if x is not None:
                heapq.heappush(f, x)
        return head.next
        