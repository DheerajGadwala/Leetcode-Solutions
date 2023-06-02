class Solution {
    public int numberOfPaths(int[][] grid, int k) {
        int mod = 1000000007;
        int m = grid.length, n = grid[0].length;
        int[][][] mem = new int[m+1][n+1][k];
        mem[0][1][0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int u = i + 1, v = j + 1;
                int val = grid[i][j];
                for (int l = 0; l < k; l++) {
                    mem[u][v][(l+val) % k] = (mem[u][v-1][l] + mem[u-1][v][l])%mod;
                }
            }
        }
        return mem[m][n][0];
    }
}