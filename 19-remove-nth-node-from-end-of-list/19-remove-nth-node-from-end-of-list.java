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
    public ListNode removeNthFromEnd(ListNode head_, int n) {
        ListNode head = new ListNode(0, head_);
        ListNode curr = head;
        int i = 0;
        while (i <= n) {
            curr = curr.next;
            i += 1;
        }
        ListNode rem = head;
        while (curr != null) {
            curr = curr.next;
            rem = rem.next;
        }
        rem.next = rem.next.next;
        return head.next;
    }
}