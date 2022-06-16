class Solution {
    public String longestPalindrome(String s) {
        
        int ans = 0, n = s.length();
        int ansLeft=0, ansRight=0;
        
        for (int i = 0; i < n; i++) {
            int o = 1;
            while (i - o > -1 && i + o < n && s.charAt(i - o) == s.charAt(i + o))
                o++;
            o--;
            if (ans < 2 * o + 1) {
                ans = 2 * o + 1;
                ansLeft = i - o;
                ansRight = i + o;
            }
            
            o = 0;
            while (i - o > -1 && i + 1 + o < n && s.charAt(i - o) == s.charAt(i + 1 + o))
                o++;
            if (ans < 2 * o) {
                ans = 2 * o;
                ansLeft = i - o + 1;
                ansRight = i + o;
            }
        }
        String ret = "";
        for (int i = ansLeft; i <= ansRight; i++) {
            ret += s.charAt(i);
        }
        System.out.println(ans + " " + ansLeft + " " + ansRight);
        return ret;
    }
}