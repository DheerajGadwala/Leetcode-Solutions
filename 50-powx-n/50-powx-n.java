class Solution {
    
    public double myPow(double x, int m) {
        long n;
        long k = (int) m;
        if (m == 0) {
            return 1;
        } 
        else if (m < 0) {
            n = -k;
        }
        else {
            n = k;
        }
        long y = 1;
        double z = x;
        double ret = 1;
        while (y <= n && y > 0) {
            if ((y & n) == y) {
                ret *= z;
            }
            y <<= 1;
            z *= z;
        }
        if (m < 0) {
            return 1/ret;
        }
        else {
            return ret;
        }
    }
}