class Solution {
    public String removeStars(String s) {
        Stack<Character> stk = new Stack<>();
        for (char c: s.toCharArray()) {
            if (c == '*') stk.pop();
            else stk.push(c);
        }
        StringBuilder ret = new StringBuilder();
        Iterator i = stk.iterator();
        while (i.hasNext()) {
            ret.append(i.next());
        }
        return ret.toString();
    }
}