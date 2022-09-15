class Solution {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int[] ret = new int[n];
        int soFar = 0, cnt = 0;
        for (int i = 0; i < n; i++) {
            ret[i] += soFar;
            if (boxes.charAt(i) == '1') cnt++;
            soFar += cnt;
        }
        soFar = 0; cnt = 0;
        for (int i = n - 1; i > -1; i--) {
            ret[i] += soFar;
            if (boxes.charAt(i) == '1') cnt++;
            soFar += cnt;
        }
        return ret;
    }
}