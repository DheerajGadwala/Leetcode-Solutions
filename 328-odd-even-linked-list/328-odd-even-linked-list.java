/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode olh = new ListNode(0), elh = new ListNode(0), ol = olh, el = elh, curr = head;
        int i = 1;
        while (curr != null) {
            if (i % 2 == 1) {
                ol.next = curr;
                ol = ol.next;
            }
            else {
                el.next = curr;
                el = el.next;
            }
            curr = curr.next;
            i++;
        }
        ol.next = elh.next;
        el.next = null;
        return olh.next;
    }
}