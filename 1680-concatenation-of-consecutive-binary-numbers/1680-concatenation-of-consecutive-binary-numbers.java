class Solution {
    public int concatenatedBinary(int n) {
        long mod = 1000000007;
        long ret = 0;
        for (int i = 1; i <= n; i++) {
            int k = i, m = 1<<20;
            boolean flag = false;
            while (m > 0) {
                if (flag) {
                    if ((m & i) != 0) {
                        ret <<= 1;
                        ret |= 1;
                        ret %= mod;
                        m >>= 1;
                    }
                    else {
                        ret <<= 1;
                        ret %= mod;
                        m >>= 1;
                    }
                }
                else if ((m & i) != 0){
                    flag = true;
                    ret <<= 1;
                    ret |= 1;
                    ret %= mod;
                    m >>= 1;
                }
                else {
                    m >>= 1;
                }
            }
        }
        return (int) ret;
    }
}