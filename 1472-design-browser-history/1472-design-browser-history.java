class BrowserHistory {

    Stack<String> b, f;
    
    public BrowserHistory(String homepage) {
        b = new Stack<>();
        f = new Stack<>();
        b.push(homepage);
    }
    
    public void visit(String url) {
        b.push(url);
        f.clear();
    }
    
    public String back(int steps) {
        while (steps-- > 0 && b.size() > 1)
            f.push(b.pop());
        return b.peek();
    }
    
    public String forward(int steps) {
        while (steps-- > 0 && f.size() > 0)
            b.push(f.pop());
        return b.peek();
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */