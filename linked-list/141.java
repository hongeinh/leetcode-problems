// https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head, slow = head;
        do {
            if (slow == null) return false;
            if (fast == null || fast.next == null) return false;
            slow = slow.next;
            fast = fast.next.next;            

        } while (slow != fast);
        return true;
    }
}