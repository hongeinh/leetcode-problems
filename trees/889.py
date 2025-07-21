# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/?envType=daily-question&envId=2025-07-21
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        index_left = self.findIndexPostOrder(preorder[1], postorder)
        root.left = self.constructFromPrePost(preorder[1:index_left + 2], postorder[:index_left + 1])
        root.right = self.constructFromPrePost(preorder[index_left + 2:], postorder[index_left + 1:-1])
        return root

    def findIndexPostOrder(self, target, postOrder):
        for i, val in enumerate(postOrder):
            if val == target:
                return i
        return -1