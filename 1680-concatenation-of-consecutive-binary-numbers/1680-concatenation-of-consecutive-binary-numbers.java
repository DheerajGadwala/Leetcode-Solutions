class Solution {
    
    static long MOD = 1000000007;
    
    public int concatenatedBinary(int n) {
        int ans = 0, firstBit = 1;
        for (int i = 1; i <= n; i++) {
            int m = firstBit;
            while (m > 0) {
                ans <<= 1;
                if ((m & i) != 0) {
                    ans |= 1;
                }
                ans %= MOD;
                m >>= 1;
            }
            if (i + 1 == (firstBit << 1)) {
                firstBit <<= 1;
            }
        }
        return ans;
    }
}