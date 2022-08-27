class Solution {
    public int maxSumSubmatrix(int[][] matrix, int t) {
        int m = matrix.length, n = matrix[0].length, ans = Integer.MIN_VALUE;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i+1][j+1] = matrix[i][j] + dp[i][j+1] + dp[i+1][j] - dp[i][j];
            }
        }
        m++; n++;
        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < m; j++) {
                for (int k = 0; k < n; k++) {
                    for (int l = k + 1; l < n; l++) {
                        int area = dp[j][l] - dp[i][l] - dp[j][k] + dp[i][k];
                        if (area <= t)
                            ans = Math.max(ans, area);
                    }
                }
            }
        }
        return ans;
    }
}