class Solution {
    
    int pos;
    String s;
    
    public String decodeString(String s) {
        pos = 0;
        this.s = s;
        this.s = "1[" + s + "]";
        return res();
    }
    
    public String res() {
        String num = "", fin = "", curr = "";
        while (pos < s.length()) {
            char c = s.charAt(pos++);
            if (c >= '0' && c <= '9') {
                fin += curr;
                curr = "";
                num += c;
            }
            else if (c >= 'a' && c <= 'z'){
                curr += c;
            }
            else if (c == '[') {
                curr = res();
                int n = Integer.parseInt(num);
                while (n > 0) {
                    fin += curr;
                    n--;
                }
                num = ""; curr = "";
            }
            else {
                return fin + curr;
            }
        }
        return fin;
    }
}