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
    
    public int minCameraCover(TreeNode root) {
        int[] ans = res(root);
        return Math.min(ans[1], ans[2]);
    }
    
    public int[] res(TreeNode node) {
        if (node == null) {
            return new int[] {0, 0, 1000};
        }
        else {
            int[] l = res(node.left);
            int[] r = res(node.right);
            int[] ret = {
                l[1] + r[1],
                Math.min(Math.min(l[2] + r[1], l[1] + r[2]), l[2] + r[2]),
                1 + Math.min(l[0], Math.min(l[1], l[2])) + Math.min(r[0], Math.min(r[1], r[2]))
            };
            return ret;
        }
    }
}