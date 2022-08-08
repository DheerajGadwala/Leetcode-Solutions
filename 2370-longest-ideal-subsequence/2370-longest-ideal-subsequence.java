class Solution {
    public int longestIdealString(String s, int k) {
        int n = s.length();
        int[] dp = new int[26];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            int best = 0;
            for (int j = Math.max(0, c - k); j < Math.min(26, c + k + 1); j++) {
                best = Math.max(best, dp[j]);
            }
            dp[c] = best + 1;
            ans = ans > dp[c] ? ans : dp[c];
        }
        return ans;
    }
}