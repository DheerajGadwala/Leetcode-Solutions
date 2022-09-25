class MyCircularQueue {
    
    int i, j, k;
    int[] q;
    boolean empty;
    
    public MyCircularQueue(int k) {
        q = new int[k];
        i=0; j=0; this.k = k;
        empty = true;
    }
    
    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        q[j] = value;
        j = (j + 1) % k;
        empty = i != j;
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        i = (i + 1) % k;
        empty = i == j;
        return true;
    }
    
    public int Front() {
        return isEmpty() ? -1 : q[i];
    }
    
    public int Rear() {
        int r = j - 1 == -1 ? k - 1 : j - 1;
        return isEmpty() ? -1 : q[r];
    }
    
    public boolean isEmpty() {
        return i==j && empty;
    }
    
    public boolean isFull() {
        return i==j && !empty;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */