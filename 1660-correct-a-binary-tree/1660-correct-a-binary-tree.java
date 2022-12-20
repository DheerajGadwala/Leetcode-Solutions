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
    
    Set<Integer> visited = new HashSet<>();
    
    public TreeNode correctBinaryTree(TreeNode root) {
        visited.clear();
        return res(root);
    }
    
    public TreeNode res(TreeNode node) {
        if (node == null) return null;
        if (node.right != null && visited.contains(node.right.val)) return null;
        node.right = res(node.right);
        visited.add(node.val);
        node.left = res(node.left);
        return node;
    }
}