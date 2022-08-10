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
    
    int[] nums;
    
    public TreeNode sortedArrayToBST(int[] nums) {
        this.nums = nums;
        return res(0, nums.length - 1);
    }
    
    private TreeNode res(int l, int h) {
        if (l == h) {
            return new TreeNode(nums[h]);
        }
        else if (l > h) {
            return null;
        }
        else {
            int m = (l + h) / 2;
            return new TreeNode(nums[m], res(l, m - 1), res(m + 1, h));
        }
    }
}