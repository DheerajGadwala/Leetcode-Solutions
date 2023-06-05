class Solution {
    public boolean checkStraightLine(int[][] coors) {
        
        int y2_m_y1 = coors[1][1] - coors[0][1];
        int x2_m_x1 = coors[1][0] - coors[0][0];
        int x1 = coors[0][0], y1 = coors[0][1];
        for (int[] coor: coors) {
            if ((coor[1] - y1) * x2_m_x1 != (coor[0] - x1) * y2_m_y1)
                return false;
        }
        return true;
    }
}