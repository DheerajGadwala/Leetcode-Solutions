class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean r = false, c = false;
        for (int i = 0; i < m; i++) 
            for (int j = 0; j < n; j++) 
                if (matrix[i][j] == 0) {
                    if (j != 0) matrix[0][j] = 0;
                    else r = true;
                    if (i != 0) matrix[i][0] = 0;
                    else c = true;
                }
        for (int i = m-1; i > -1; i--) 
            for (int j = n-1; j > -1; j--)
                if (matrix[i][0] == 0 || matrix[0][j] == 0) matrix[i][j] = 0;
                else if ((i == 0 && c) || (j == 0 && r)) matrix[i][j] = 0;
    }
}