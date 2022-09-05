/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        
        Deque<Node> q = new LinkedList<>();
        List<List<Integer>> ans = new ArrayList<>();
        
        if (root != null) {
            q.add(root);
            ans.add(new ArrayList<>());   
        }
        
        Node last = root;
        int level = 0;
        
        while (q.size() != 0) {
            
            Node u = q.poll();
            ans.get(ans.size()-1).add(u.val);
            
            for (Node l: u.children) {    
                q.add(l);
            }
            
            if (u == last && q.size() > 0) {
                ans.add(new ArrayList<>());
                last = q.getLast();
            }
            
        }
        
        return ans;
        
    }
}