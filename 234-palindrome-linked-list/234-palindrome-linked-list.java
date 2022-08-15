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
    public boolean isPalindrome(ListNode head) {
        ListNode one = head, two = head;
        while (two != null && two.next != null) {
            one = one.next;
            two = two.next.next;
        }
        ListNode prev = null, curr = one;
        while (curr.next != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        curr.next = prev;
        ListNode start = head, end = curr;
        while (start != one) {
            if (start.val != end.val) {
                return false;
            }
            start = start.next;
            end = end.next;
        }
        return true;
    }
}