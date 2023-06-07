class Solution {
    public int minFlips(int a, int b, int c) {
        int fc = 0;
        int i = 1;
        while (i <= a || i <= b || i <= c) {
            if ((i & (a | b)) == (i & c)) {
            }
            else if ((i & c) == 0) {
                fc += (a & i) != 0 ? 1 : 0;
                fc += (b & i) != 0 ? 1 : 0;
            }
            else {
                fc += 1;
            }
            i <<= 1;
        }
        return fc;
    }
}