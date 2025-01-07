# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        level = 0
        if not root:
            return level
        queue = [root]
        while queue:
            level += 1
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                for child in cur.children:
                    queue.append(child)
        return level