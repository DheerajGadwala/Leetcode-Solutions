class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> ss = new Stack<>(), ts = new Stack<>();
        for (char c: s.toCharArray()) {
            if (c == '#' && ss.size() != 0) {
                ss.pop();
            }
            else if (c != '#'){
                ss.push(c);
            }
        }
        for (char c: t.toCharArray()) {
            if (c == '#' && ts.size() != 0) {
                ts.pop();
            }
            else if (c != '#') {
                ts.push(c);
            }
        }
        if (ss.size() != ts.size()) {
            return false;
        }
        else {
            while (ss.size() != 0) {
                if (ss.pop() != ts.pop()) {
                    return false;
                }
            }
            return true;
        }
    }
}