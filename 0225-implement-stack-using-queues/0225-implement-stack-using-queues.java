class MyStack {

    Queue<Integer> q;
    
    public MyStack() {
        q = new LinkedList<>();
    }
    
    public void push(int x) {
        q.add(x);
    }
    
    public int pop() {
        int n = q.size();
        for (int i = 0; i < n-1; i++) 
            q.add(q.poll());
        return q.poll();
    }
    
    public int top() {
        int n = q.size();
        for (int i = 0; i < n-1; i++)
            q.add(q.poll());
        int ret = q.poll();
        q.add(ret);
        return ret;
    }
    
    public boolean empty() {
        return q.size() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */