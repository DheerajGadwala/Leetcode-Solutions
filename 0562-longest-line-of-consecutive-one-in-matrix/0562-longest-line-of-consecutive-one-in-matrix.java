class Solution {
    
    
    private int[][] copy(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[][] ret = new int[m+2][n+2];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ret[i+1][j+1] = mat[i][j];
            }
        }
        return ret;
    }
    
    public int longestLine(int[][] mat) {
        int[][] c = copy(mat);
        int ret = 0;
        int m = mat.length+1, n = mat[0].length+1;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (c[i][j] != 0)
                    c[i][j] += c[i][j-1];
                ret = Math.max(ret, c[i][j]);
            }
        }
        c = copy(mat);
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (c[j][i] != 0)
                    c[j][i] += c[j-1][i];
                ret = Math.max(ret, c[j][i]);
            }
        }
        c = copy(mat);
        for (int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                if (c[i][j] != 0)
                    c[i][j] += c[i-1][j-1];
                ret = Math.max(ret, c[i][j]);
            }
        }
        c = copy(mat);
        for (int i = m; i > 0; i--) {
            for (int j = 0; j < n ; j++) {
                if (c[i][j] != 0)
                    c[i][j] += c[i+1][j-1];
                ret = Math.max(ret, c[i][j]);
            }
        }
        return ret;
    }
}