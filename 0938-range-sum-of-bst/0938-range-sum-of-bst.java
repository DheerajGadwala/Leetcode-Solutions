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
    public int rangeSumBST(TreeNode node, int low, int high) {
        if (node == null) {
            return 0;
        }
        else if (low <= node.val && node.val <= high) {
            return node.val + rangeSumBST(node.left, low, high) + rangeSumBST(node.right, low, high);
        }
        else if (low > node.val) {
            return rangeSumBST(node.right, low, high);
        }
        else if (node.val > high) {
            return rangeSumBST(node.left, low, high);
        }
        else {
            return 0;
        }
    }
}