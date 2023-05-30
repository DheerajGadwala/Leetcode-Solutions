class Node {
    
    public int val;
    public Node next;
    
    public Node(int val) {
        this.val = val;
        this.next = null;
    }
    
    public Node(int val, Node node) {
        this.val = val;
        this.next = node;
    }
}

class MyHashSet {

    static int size = 10091;
    Node[] map;
    
    public MyHashSet() {
        map = new Node[size];
        for (int i = 0; i < size; i++)
            map[i] = new Node(-1);
    }
    
    public void add(int key) {
        int slot = Objects.hash(key) % size;
        if (!contains(key))
            map[slot].next = new Node(key, map[slot].next);
    }
    
    public void remove(int key) {
        int slot = Objects.hash(key) % size;
        Node curr = map[slot];
        while (curr.next != null) {
            if (curr.next.val == key) {
                curr.next = curr.next.next;
                break;
            }
            curr = curr.next;
        }
    }
    
    public boolean contains(int key) {
        int slot = Objects.hash(key) % size;
        Node curr = map[slot];
        while (curr.next != null) {
            if (curr.next.val == key) {
                return true;
            }
            curr = curr.next;
        }
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */