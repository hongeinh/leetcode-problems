# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        """

        remember = 0
        end = 0
        result = []

        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + remember
            remember = 1 if sum >= 10 else 0
            result.append(sum%10)
            if l1.next is None:
                end = 1
            elif l2.next is None:
                end = 2
            l1 = l1.next
            l2 = l2.next

        if end == 2:
            while l1 is not None:
                sum = 0
                sum = l1.val + remember
                remember = 1 if sum >= 10 else 0
                result.append(sum%10)
                l1 = l1.next
        elif end == 1:
            while l2 is not None:
                sum = 0
                sum = l2.val + remember
                remember = 1 if sum >= 10 else 0
                result.append(sum%10)
                l2 = l2.next

        if remember != 0:
            result.append(remember)
        
        prev = None
        node = None
        for i in reversed(range(len(result))):
            node = ListNode(result[i], prev)
            prev = node
        return node

sol = Solution()

def create_list(arr):
    prev = None
    node = None
    for i in reversed(range(len(arr))):
        node = ListNode(arr[i], prev)
        prev = node
    return node
# print(sol.addTwoNumbers([2,4,3], [5,6,4]))
# print(sol.addTwoNumbers([0], [0]))
print(sol.addTwoNumbers(create_list([2,4,9]), create_list([5,6,4,9])))
        