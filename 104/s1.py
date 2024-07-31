# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        count = 0
        return self.maxDepthHelper(root, count)

    def maxDepthHelper(self, curr, count):
        if curr is None:
            return count
        else:
            count += 1
        leftDepth = self.maxDepthHelper(curr.left, count)
        rightDepth = self.maxDepthHelper(curr.right, count)
        return max(leftDepth, rightDepth)

        