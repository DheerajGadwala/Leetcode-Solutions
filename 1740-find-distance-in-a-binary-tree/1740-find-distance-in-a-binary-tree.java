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
    int ph = 0, qh = 0, ah = 0, p, q;
    public int findDistance(TreeNode root, int p, int q) {
        this.p = p;
        this.q = q;
        res(root, 0);
        return ph + qh - 2*ah;
    }
    private TreeNode res(TreeNode node, int h) {
        if (node == null) {
            return null;
        }
        else {
            TreeNode left = res(node.left, h+1);
            TreeNode right = res(node.right, h+1);
            if (left != null && right != null) ah = h;
            else if ((node.val == p || node.val == q) && (left != null || right != null)) ah = h;
            else if (node.val == p && node.val == q) ah = h;
            if (node.val == p) ph = h;
            if (node.val == q) qh = h;
            if (node.val == p || node.val == q) return node;
            else if (left != null) return left;
            else if (right != null) return right;
            else return null;
        }
    }
    
    
}