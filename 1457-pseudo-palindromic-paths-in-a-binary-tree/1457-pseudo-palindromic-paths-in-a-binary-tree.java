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
        return res(root, new int[10]);
    }
    
    private int res(TreeNode node, int[] acc) {
        if (node == null) {
            return 0;
        }
        else if (node.left == null && node.right == null) {
            acc[node.val]++;
            return isPseudoPalindromic(acc) ? 1 : 0;
        }
        else {
            acc[node.val]++;
            return res(node.left, deepCopy(acc)) + res(node.right, deepCopy(acc));
        }
    }
    
    private int[] deepCopy(int[] arr) {
        int[] copy = new int[10];
        for (int i = 0; i < 10; i++) {
            copy[i] = arr[i];
        }
        return copy;
    }
    
    private boolean isPseudoPalindromic(int[] arr) {
        int oddCount = 0;
        for (int k: arr) {
            oddCount += k % 2 == 1 ? 1 : 0;
        }
        return oddCount < 2;
    }
}