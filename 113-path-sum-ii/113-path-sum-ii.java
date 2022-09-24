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
    
    int target;
    List<List<Integer>> paths;
    
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        this.target = targetSum;
        this.paths = new ArrayList<>();
        res(root, 0, new ArrayList<>());
        return paths;
    }
    
    private void res(TreeNode node, int sum, List<Integer> path) {
        if (node == null) {
            return;
        }
        else if (node.left == null && node.right == null && sum + node.val == target) {
            path.add(node.val);
            paths.add(path);
        }
        else {
            path.add(node.val);
            List<Integer> l = new ArrayList<>(path), r = new ArrayList<>(path);
            res(node.left, sum + node.val, l);
            res(node.right, sum + node.val, r);
        }
    }
}