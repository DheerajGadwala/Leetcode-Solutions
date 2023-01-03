class Solution {
    public int minDeletionSize(String[] strs) {
        int del = 0, m = strs.length, n = strs[0].length();
        for (int i = 0; i < n; i++) {
            char prev = 'a';
            for (int j = 0; j < m; j++) {
                char curr = strs[j].charAt(i);
                if (curr < prev) {
                    del++;
                    break;
                }
                prev = curr;
            }
        }
        return del;
    }
}