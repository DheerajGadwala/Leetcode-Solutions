class Solution {
    
    int[][] mat;
    
    public int[][] diagonalSort(int[][] mat) {
        this.mat = mat;
        for (int i = 1; i < mat.length; i++) {
            bubble(i, 0);
        }
        for (int j = 1; j < mat[0].length; j++) {
            bubble(0, j);
        }
        bubble(0, 0);
        return mat;
    }
    
    private void bubble(int i, int j) {
        int m = mat.length, n = mat[0].length;
        int r = i, s = j;
        while (r < m && s < n) {
            int p = i+1, q = j+1;
            while (p < m && q < n) {
                if (mat[p][q] < mat[p-1][q-1]) {
                    int temp = mat[p][q];
                    mat[p][q] = mat[p-1][q-1];
                    mat[p-1][q-1] = temp;
                }
                p++; q++;
            }
            r++; s++;
        }
    }
}