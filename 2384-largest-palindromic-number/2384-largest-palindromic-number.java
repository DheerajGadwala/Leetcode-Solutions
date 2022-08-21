class Solution {
    public String largestPalindromic(String num) {
        int[] cnt = new int[10];
        for (int i = 0; i < num.length(); i++) {
            cnt[num.charAt(i) - '0'] += 1;
        }
        StringBuilder l = new StringBuilder(), r = new StringBuilder();
        int center = -1;
        for (int i = 9; i > 0; i--) {
            while (cnt[i] > 1) {
                cnt[i] -= 2;
                l.append(i);
                r.insert(0, i);
            }
            if (cnt[i] == 1 && center == -1) {
                center = i;
            }
        }
        if (l.length() > 0) {
            while (cnt[0] > 1) {
                cnt[0] -= 2;
                l.append(0);
                r.insert(0, 0);
            }
            if (cnt[0] == 1 && center == -1) {
                center = 0;
            }
        }
        if (center == -1 && l.length() == 0)
            return "0";
        if (center != -1)
            return l.toString() + center + r.toString();
        else
            return l.toString() + r.toString();
    }
}