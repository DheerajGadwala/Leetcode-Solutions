class Solution {
    
    int pos;
    String s;
    
    public String decodeString(String s) {
        pos = 0;
        this.s = s;
        this.s = "1[" + s + "]";
        return res().toString();
    }
    
    public StringBuilder res() {
        StringBuilder num = new StringBuilder(), fin = new StringBuilder(), curr = new StringBuilder();
        while (pos < s.length()) {
            char c = s.charAt(pos++);
            if (c >= '0' && c <= '9') {
                fin.append(curr);
                curr = new StringBuilder();
                num.append(c);
            }
            else if (c >= 'a' && c <= 'z'){
                curr.append(c);
            }
            else if (c == '[') {
                curr = res();
                int n = Integer.parseInt(num.toString());
                while (n > 0) {
                    fin.append(curr);
                    n--;
                }
                num = new StringBuilder(); curr = new StringBuilder();
            }
            else {
                fin.append(curr);
                return fin;
            }
        }
        return fin;
    }
}