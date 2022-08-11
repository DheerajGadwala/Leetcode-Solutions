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
    public boolean isValidBST(TreeNode root) {
        return res(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    boolean res(TreeNode node, long minSoFar, long maxSoFar) {
        if (node == null) {
            return true;
        }
        else {
            return node.val < maxSoFar && node.val > minSoFar && res(node.left, minSoFar, node.val) && res(node.right, node.val, maxSoFar);
        }
    }
}