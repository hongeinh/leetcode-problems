# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        self.head = self
        self.tail = self 
        self.len = 1

    def appendNode(self, val):
        node = ListNode(val)
        self.tail.next = node
        self.tail = node
        self.len += 1

    def traverse(self):
        curr_node = self.head
        while(curr_node != None):
            print(curr_node.val)
            curr_node = curr_node.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pass

    def sortArray(self, l1, l2):
        # if len(l1) >= len(2):
        pass

l1 = [4, 3]
first = ListNode(2)
for val in l1:
    first.appendNode(val)
first.traverse()

        