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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
        head = new ListNode(0, head);
        
        ListNode curr = head;
        
        for (int i = 0; i < left - 1; i++) {
            curr = curr.next;
        }
        
        ListNode rev = curr.next;
        ListNode t = curr.next;
        ListNode prev = null;
        
        for (int i = left - 1; i < right; i++) {
            ListNode temp = rev.next;
            rev.next = prev;
            prev = rev;
            rev = temp;
        }
        
        curr.next = prev;
        t.next = rev;
        
        return head.next;
        
    }
}