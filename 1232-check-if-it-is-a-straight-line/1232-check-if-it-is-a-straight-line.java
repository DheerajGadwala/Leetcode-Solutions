class Solution {
    public boolean checkStraightLine(int[][] coors) {
        if (coors[1][0] == coors[0][0]) {
            boolean ret = true;
            for (int[] v: coors) {
                ret &= v[0] == coors[1][0];
            }
            return ret;
        }
        double m = 1.0*(coors[1][1] - coors[0][1]) / (coors[1][0] - coors[0][0]);
        double c = coors[0][1] - coors[0][0] * m;
        boolean ret = true;
        for (int[] v: coors) {
            ret &= v[1] == m * v[0] + c;
        }
        return ret;
    }
}