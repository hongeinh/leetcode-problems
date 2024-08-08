# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != slow or fast is None:
            slow = slow.next
            if slow.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return fast.val
        return -1