class Node {
    
    Node next, prev;
    int val, key;
    
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
    
}

class LRUCache {

    
    Map<Integer, Node> cache;
    Node head, tail;
    int capacity;
    
    public LRUCache(int capacity) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
        cache = new HashMap<>();
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;
        Node node = cache.get(key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
        return node.val;
    }
    
    public void put(int key, int value) {
        if (!cache.containsKey(key)) {
            if (capacity == 0) {
                cache.remove(tail.prev.key);
                tail.prev.prev.next = tail;
                tail.prev = tail.prev.prev;  
            }
            else {
                capacity--;
            }
            Node node = new Node(key, value);
            node.next = head.next;
            node.prev = head;
            head.next.prev = node;
            head.next = node;
            cache.put(key, node);
        }
        else {
            Node node = cache.get(key);
            node.val = value;
            node.prev.next = node.next;
            node.next.prev = node.prev;
            node.next = head.next;
            head.next.prev = node;
            node.prev = head;
            head.next = node;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */