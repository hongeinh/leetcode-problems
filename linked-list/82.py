# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        cur = head.next
        prev = head
        prev_val = prev.val
        is_dup = False
        while cur is not None:
            if cur.val == prev.val:
                prev.next = cur.next
                tmp = cur.next
                cur.next = None
                cur = tmp
                is_dup = True
                continue
            if is_dup :
                cur = cur.next
                prev.next = cur
                is_dup = False
            else: 
                prev = cur
                prev_val = prev.val
                cur = cur.next
        return head
        