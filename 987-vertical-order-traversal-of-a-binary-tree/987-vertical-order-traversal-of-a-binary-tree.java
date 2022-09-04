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
    
    static Map<Integer, List<Integer>> DEFAULT = new HashMap<>();
    Map<Integer, Map<Integer, List<Integer>>> store;
    int minX, minY, maxX, maxY;
    
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        store = new HashMap<>();
        minX = 0; maxX = 0; minY = 0; maxY = 0;
        res(root, 0, 0);
        List<List<Integer>> ret = new ArrayList<>();
        for (int j = minY; j <= maxY; j++) {
            List<Integer> curr = new ArrayList<>();
            for (int i = minX; i <= maxX; i++) {
                if (store.getOrDefault(i, DEFAULT).containsKey(j)) {
                    Collections.sort(store.get(i).get(j));
                    curr.addAll(store.get(i).get(j));
                }
            }
            if (curr.size() != 0) {
                ret.add(curr);
            }
        }
        return ret;
    }
    
    private void res(TreeNode node, int x, int y) {
        if (node != null) {
            if (!store.containsKey(x)) {
                store.put(x, new HashMap<>());
            }
            if (!store.get(x).containsKey(y)) {
                store.get(x).put(y, new ArrayList());
            }
            store.get(x).get(y).add(node.val);
            minX = Math.min(minX, x);
            minY = Math.min(minY, y);
            maxX = Math.max(maxX, x);
            maxY = Math.max(maxY, y);
            res(node.left, x + 1, y - 1);
            res(node.right, x + 1, y + 1);
        }
    }
}