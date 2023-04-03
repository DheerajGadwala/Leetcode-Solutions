class Solution {
    public int ways(String[] pizza, int k) {
        int mod = 1000000007;
        int m = pizza.length, n = pizza[0].length();
        int[][] grid = new int[m+1][n+1];
        int[][][] dp = new int[m+1][n+1][k];
        for (int i = m - 1; i > -1; i--) {
            for (int j = n - 1; j > -1; j--) {
                grid[i][j] = pizza[i].charAt(j) == 'A' ? 1 : 0;
                grid[i][j] += grid[i+1][j] + grid[i][j+1] - grid[i+1][j+1];
                dp[i][j][0] = grid[i][j] == 0 ? 0 : 1;
            }
        }
        for (int p = 1; p < k; p++) {
            for (int q = m - 1; q > -1; q--) {
                for (int r = n - 1; r > -1; r--) {
                    for (int s = q + 1; s < m; s++) {
                        int apples = grid[q][r] - grid[s][r];
                        if (apples > 0) dp[q][r][p] += dp[s][r][p-1];
                        dp[q][r][p] %= mod;
                    }
                    for (int s = r + 1; s < n; s++) {
                        int apples = grid[q][r] - grid[q][s];
                        if (apples > 0) dp[q][r][p] += dp[q][s][p-1];
                        dp[q][r][p] %= mod;
                    }
                }
            }
        }
        return dp[0][0][k-1];
        
    }
}