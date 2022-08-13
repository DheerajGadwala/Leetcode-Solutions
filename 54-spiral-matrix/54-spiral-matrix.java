class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[][] d = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int i = 0, j = 0, dir = 0;
        List<Integer> ret = new ArrayList<>();
        boolean flag = true;
        while (true) {
            if (flag) {
                ret.add(matrix[i][j]);
                matrix[i][j] = -101;
            }
            int ni = d[dir][0] + i, nj = d[dir][1] + j;
            if (ni > -1 && nj > -1 && ni < m && nj < n && matrix[ni][nj] != -101) {
                i = ni;
                j = nj;
                flag = true;
            }
            else {
                if (!flag) {
                    break;
                }
                dir = (dir + 1) % 4;
                flag = false;
            }
        }
        return ret;
    }
}