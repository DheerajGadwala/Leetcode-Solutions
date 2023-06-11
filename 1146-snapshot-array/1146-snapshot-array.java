class Node {
    int id, val;
    
    Node(int id, int val) {
        this.id = id;
        this.val = val;
    }
    
    @Override
    public String toString() {
        return id + " " + val + ";";
    }
}

class SnapshotArray {
    
    List<Node>[] arr;
    int id;
    
    public SnapshotArray(int length) {
        arr = new ArrayList[length];
        for (int i = 0; i < length; i++) {
            arr[i] = new ArrayList<>();
            arr[i].add(new Node(0, 0));
        }
        id = 0;
    }
    
    public void set(int index, int val) {
        int n = arr[index].size() - 1;
        if (arr[index].get(n).id == id)
            arr[index].get(n).val = val;
        else
            arr[index].add(new Node(id, val));
    }
    
    public int snap() {
        id++;
        return id - 1;
    }
    
    public int get(int index, int snap_id) {
        List<Node> l = arr[index];
        int low = 0, high = l.size() - 1;
        int ans = 0;
        while (low <= high) {
            int mid = (low + high) / 2;
            int curr = l.get(mid).id;
            // if (curr == snap_id) ans = mid;
            if (curr <= snap_id) {ans = mid; low = mid + 1;}
            else high = mid - 1;
            
        }
        return l.get(ans).val;
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */