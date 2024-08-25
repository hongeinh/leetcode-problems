# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/reverse-linked-list-ii/
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
        
        # Initialize dummy node
        dummy = ListNode(0, head)

        # Find left - 1 node
        prev = dummy
        for _ in range(left-1):
            print(prev.val)
            prev = prev.next
        
        cur = prev.next

        # Reverse
        for _ in range(right - left):
            next_node = cur.next
            cur.next = next_node.next  # Reverse the link
            next_node.next = prev.next  # Insert current node after the previous node
            prev.next = next_node  # Update the previous node's next pointer


        return dummy.next
