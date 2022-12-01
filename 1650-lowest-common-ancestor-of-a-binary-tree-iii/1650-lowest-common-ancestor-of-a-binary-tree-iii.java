/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {
        int hp = 0, hq = 0;
        Node pc = p, qc = q;
        while (pc != null) {
            pc = pc.parent;
            hp++;
        }
        while (qc != null) {
            qc = qc.parent;
            hq++;
        }
        if (hp > hq) {
            int temp = hq;
            hq = hp;
            hp = temp;
            Node tempN = q;
            q = p;
            p = tempN;
        }
        while (hp != hq) {
            q = q.parent;
            hq--;
        }
        while (p != q) {
            p = p.parent;
            q = q.parent;
        }
        return p;
    }
}