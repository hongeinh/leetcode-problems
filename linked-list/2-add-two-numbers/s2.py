# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        carry = 0
        rhead = l1
        rtail = l1
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            carry = 1 if sum >= 10 else 0
            rtail.val = sum%10
            l1 = l1.next
            l2 = l2.next
            rtail.next = l1 if l2 is None else l2
            rtail = rtail.next if rtail.next is not None else rtail
        while l1 is not None:
            sum = l1.val + carry
            carry = 1 if sum >= 10 else 0
            rtail.val = sum%10
            l1 = l1.next
            rtail = l1 if l1 is not None else rtail
        while l2 is not None:
            sum = l2.val + carry
            carry = 1 if sum >= 10 else 0
            rtail.val = sum%10
            l2 = l2.next
            rtail = l2 if l2 is not None else rtail
        if carry == 1:
            rtail.next = ListNode(1)
        return rhead 