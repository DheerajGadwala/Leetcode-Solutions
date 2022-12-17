class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<>();
        for (String token: tokens) {
            try {
                int x = Integer.parseInt(token);
                s.push(x);
            }
            catch (Exception e) {
                int a = s.pop(), b = s.pop();
                if (token.equals("+")) s.push(a+b);
                else if (token.equals("/")) s.push(b/a);
                else if (token.equals("-")) s.push(-a+b);
                else if (token.equals("*")) s.push(a*b);
            }
        }
        return s.pop();
    }
}