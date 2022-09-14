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
    public int pseudoPalindromicPaths (TreeNode root) {
        return res(root, new HashMap<>());
    }
    
    public int res(TreeNode node, Map<Integer, Integer> acc) {
        if (node == null) {
            return 0;
        }
        else {
            acc.put(node.val, acc.getOrDefault(node.val, 0) + 1);
        }
        if (node.left == null && node.right == null) {
            int oddCount = 0;
            for (int k: acc.values()) {
                oddCount += k % 2 == 1 ? 1 : 0;
            }
            return oddCount > 1 ? 0 : 1;
        }
        else {
            Map<Integer, Integer> leftCopy = new HashMap<>(acc), rightCopy = new HashMap<>(acc);
            return res(node.left, leftCopy) + res(node.right, rightCopy);
        }
    }
}