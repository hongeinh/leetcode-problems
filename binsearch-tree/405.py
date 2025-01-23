# https://leetcode.com/problems/delete-node-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # find successor
            successor = root.right
            while successor and successor.left:
                successor = successor.left
            root.val = successor.val
            root.right =  self.deleteNode(root.right, successor.val)
        return root