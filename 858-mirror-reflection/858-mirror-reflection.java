class Solution {
    public int mirrorReflection(int p, int q) {
        int x = p;
        int y = q;
        while(x%2 == 0 && y%2 == 0) {
            x /= 2;
            y /= 2;
        }
        return x % 2 == 1 && y % 2 == 1 ? 1 : y % 2 == 1 ? 2 : 0;
    }
}