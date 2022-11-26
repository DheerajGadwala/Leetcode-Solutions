/**
 * This is the interface for the expression tree Node.
 * You should not remove it, and you can define some classes to implement it.
 */

abstract class Node {
    Node left, right;
    public abstract int evaluate();
    // define your fields here
};

class val extends Node{
    
    int value;
    
    public val(int value) {
        this.value = value;
    }
    
    public int evaluate() {return value;}
}

class div extends Node{
    public div(Node left, Node right) {
        this.left = left;
        this.right = right;
    }
    
    public int evaluate() {return left.evaluate() / right.evaluate();}
}

class mul extends Node{
    public mul(Node left, Node right) {
        this.left = left;
        this.right = right;
    }
    
    public int evaluate() {return left.evaluate() * right.evaluate();}
}

class plus extends Node{
    public plus(Node left, Node right) {
        this.left = left;
        this.right = right;
    }
    
    public int evaluate() {return left.evaluate() + right.evaluate();}
}

class minus extends Node{
    public minus(Node left, Node right) {
        this.left = left;
        this.right = right;
    }
    
    public int evaluate() {return left.evaluate() - right.evaluate();}
}


/**
 * This is the TreeBuilder class.
 * You can treat it as the driver code that takes the postinfix input 
 * and returns the expression tree represnting it as a Node.
 */

class TreeBuilder {
    Node buildTree(String[] postfix) {
        Stack<Node> s = new Stack<>();
        for (String k: postfix) {
            Node l, r;
            if (k.equals("*")) {
                r = s.pop(); l = s.pop();
                s.push(new mul(l, r));
            }
            else if (k.equals("/")){
                r = s.pop(); l = s.pop();
                s.push(new div(l, r));
            }
            else if (k.equals("+")){
                r = s.pop(); l = s.pop();
                s.push(new plus(l, r));
            }
            else if (k.equals("-")){
                r = s.pop(); l = s.pop();
                s.push(new minus(l, r));
            }
            else {
                s.push(new val(Integer.parseInt(k)));
            }
        }
        return s.pop();
    }
};


/**
 * Your TreeBuilder object will be instantiated and called as such:
 * TreeBuilder obj = new TreeBuilder();
 * Node expTree = obj.buildTree(postfix);
 * int ans = expTree.evaluate();
 */