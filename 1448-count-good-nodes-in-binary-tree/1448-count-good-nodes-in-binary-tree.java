/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int goodNodes(TreeNode root) {
        return res(root, Integer.MIN_VALUE);
    }
    
    private int res(TreeNode node, int max) {
        if (node == null) {
            return 0;
        }
        else if (node.val >= max) {
            return 1 + res(node.left, node.val) + res(node.right, node.val);
        }
        else {
            return res(node.left, max) + res(node.right, max);
        }
    }
}