# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head.next
        prev = head
        prev_val = prev.val
        while cur is not None:
            if cur.val == prev.val:
                prev.next = cur.next
                tmp = cur.next
                cur.next = None
                cur = tmp
            else:
                prev = cur
                prev_val = prev.val 
                cur = cur.next
        return head


        