class Solution {
    public long gridGame(int[][] g) {
        int n = g[0].length;
        long[][] grid = new long[2][n];
        for (int i = 0; i < n; i++) {
            grid[0][i] = g[0][i];
            grid[1][i] = g[1][i];
        }
        for (int i = 1; i < n; i++) {
            grid[0][i] += grid[0][i-1];
        }
        for (int i = n - 2; i > -1; i--) {
            grid[1][i] += grid[1][i+1];
        }
        long ans = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            ans = Math.min(ans, Math.max(grid[0][n-1] - grid[0][i], grid[1][0] - grid[1][i]));
        }
        return ans;
    }
}