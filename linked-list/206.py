# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/reverse-linked-list/description/
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        prev, cur = None, head
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev