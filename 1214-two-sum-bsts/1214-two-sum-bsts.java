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
    
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        List<Integer> l1 = new ArrayList<>(), l2 = new ArrayList<>();
        inorder(root1, l1);
        inorder(root2, l2);
        int m = l1.size(), n = l2.size();
        int i = 0, j = n - 1;
        while (i < m && j > -1) {
            if (l1.get(i) + l2.get(j) == target) return true;
            else if (l1.get(i) + l2.get(j) < target) i++;
            else j--;
        }
        i = m - 1;
        j = 0;
        while (i > -1 && j < n) {
            if (l1.get(i) + l2.get(j) == target) return true;
            else if (l1.get(i) + l2.get(j) < target) j++;
            else i--;
        }
        return false;
    }
    
    public void inorder(TreeNode root, List<Integer> l) {
        if (root == null) return;
        inorder(root.left, l);
        l.add(root.val);
        inorder(root.right, l);
    }
}