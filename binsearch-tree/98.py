# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.MAX = 10E9
        self.MIN = -10E9
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, self.MAX, self.MIN)
    
    def dfs(self, root, max_val, min_val):
        if not root:
            return True
        if root.val >= max_val or root.val <= min_val:
            return False
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.dfs(root.left, root.val, min_val) and self.dfs(root.right, max_val, root.val)
        