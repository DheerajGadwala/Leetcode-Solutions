class Solution {
    public boolean checkStraightLine(int[][] coors) {
        if (coors[1][0] == coors[0][0]) {
            for (int[] v: coors) {
                if (v[0] != coors[1][0])
                    return false;
            }
            return true;
        }
        double m = 1.0*(coors[1][1] - coors[0][1]) / (coors[1][0] - coors[0][0]);
        double c = coors[0][1] - coors[0][0] * m;
        for (int[] v: coors) {
            if (v[1] != m * v[0] + c)
                return false;
        }
        return true;
    }
}