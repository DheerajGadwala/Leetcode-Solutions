class Solution {
    public String shortestCommonSupersequence(String s1, String s2) {
        String s3 = lcs(s1, s2);
        int i = 0, j = 0, k = 0;
        String ans = "";
        while (i < s1.length() && j < s2.length() && k < s3.length()) {
            if (s3.charAt(k) == s1.charAt(i) && s3.charAt(k) == s2.charAt(j)) {
                ans += s3.charAt(k);
                i++;j++;k++;
            }
            else if (s3.charAt(k) == s1.charAt(i)) {
                ans += s2.charAt(j);
                j++;
            }
            else if (s3.charAt(k) == s2.charAt(j)) {
                ans += s1.charAt(i);
                i++;
            }
            else {
                ans += s1.charAt(i);
                ans += s2.charAt(j);
                i++;j++;
            }
        }
        while (i < s1.length()) {
            ans += s1.charAt(i);
            i++;
        }
        while (j < s2.length()) {
            ans += s2.charAt(j);
            j++;
        } 
        return ans;
    }
    
    public String lcs(String s1, String s2) {
        int[][] dp = new int[s1.length()+1][s2.length()+1];
        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
                if (s1.charAt(i) == s2.charAt(j)) {
                    dp[i+1][j+1] = Math.max(dp[i][j] + 1, dp[i+1][j+1]);
                }
                else {
                    dp[i+1][j+1] = Math.max(dp[i][j], dp[i+1][j+1]);
                }
            }
        }
        int i = s1.length(), j = s2.length();
        String ans = "";
        while (i != 0 && j != 0) {
            if (i > 0 && j > 0 && dp[i-1][j-1] >= dp[i][j-1] && dp[i-1][j-1] >= dp[i-1][j]) {
                ans = dp[i-1][j-1] != dp[i][j] ? s1.charAt(i-1) + ans : ans;
                i--;j--;
            }
            else if (j > 0 && i > 0 && dp[i][j-1] >= dp[i-1][j]) {
                j--;
            }
            else if (i > 0) {
                i--;
            }
        }
        return ans;
    }
}