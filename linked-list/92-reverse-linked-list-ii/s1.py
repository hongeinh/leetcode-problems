# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return head
        node = ListNode(0)
        node.next = head
        prev = node
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next

        for _ in range(right - left):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = tmp

        prev.next = curr

        return head
