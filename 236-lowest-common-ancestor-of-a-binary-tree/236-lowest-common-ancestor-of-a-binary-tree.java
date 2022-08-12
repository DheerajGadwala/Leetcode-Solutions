/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode s) {
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        Map<TreeNode, Integer> level = new HashMap<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        level.put(root, 0);
        while (q.size() != 0) {
            TreeNode u = q.poll();
            if (u.left != null) {
                q.add(u.left);
                parent.put(u.left, u);
                level.put(u.left, level.get(u) + 1);
            }
            if (u.right != null) {
                q.add(u.right);
                parent.put(u.right, u);
                level.put(u.right, level.get(u) + 1);
            }
        }
        while (level.get(p) > level.get(s)) {
            p = parent.get(p);
        }
        while (level.get(s) > level.get(p)) {
            s = parent.get(s);
        }
        while (p != s) {
            p = parent.get(p);
            s = parent.get(s);
        }
        return p;
    }
}