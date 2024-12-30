
import java.util.HashMap;

// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
// Question: do the items in the tree have unique values ?
public class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Create a map to store values and their corresponding index in the inorder array
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int idx = 0; idx < inorder.length; idx++) {
            map.put(inorder[idx], idx);
        }

        // needs to be an array because int is primitive and it pass by value
        // changes wont be updated outside the scope of the function 
        int[] index = {0};

        return helper(preorder, inorder, 0, preorder.length - 1, map, index);
    }

    public TreeNode helper(int[] preorder, int[] inorder, int left, int right,
            HashMap<Integer, Integer> map, int[] index) {

        // no more items to check
        if (left > right) {
            return null;
        }

        int curr = preorder[index[0]];
        index[0]++;

        TreeNode node = new TreeNode(curr);

        if (left == right) {
            return node;
        }

        int inorderIndex = map.get(curr);
        node.left = helper(preorder, inorder, left, inorderIndex - 1, map, index);
        node.right = helper(preorder, inorder, inorderIndex + 1, right, map, index);

        return node;
    }

}
