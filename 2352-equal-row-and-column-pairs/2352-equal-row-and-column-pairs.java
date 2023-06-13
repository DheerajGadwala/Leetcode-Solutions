class Solution {
    public int equalPairs(int[][] grid) {
        int ans = 0;
        int n = grid[0].length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                boolean flag = true;
                for (int k = 0; k < n; k++) {
                    flag &= grid[i][k] == grid[k][j];
                }
                if (flag)
                    ans++;
            }
        }
        return ans;
    }
}