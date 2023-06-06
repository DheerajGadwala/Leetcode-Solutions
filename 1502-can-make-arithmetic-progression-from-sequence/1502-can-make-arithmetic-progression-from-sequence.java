class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        int max = arr[0], min = arr[0], n = arr.length;
        for (int i: arr) {
            max = Math.max(i, max);
            min = Math.min(i, min);
        }
        double ddiff = 1.0 * (max - min) / (n - 1);
        int diff = (int) ddiff;
        if (ddiff != diff) return false;
        if (diff == 0) return true;
        for (int i = 0; i < n;) {
            int val = arr[i];
            double dpos = 1.0 * (val - min) / diff;
            int pos = (int) dpos;
            if (pos != dpos || dpos < 0 || dpos >= n) {
                return false;
            }
            else if (pos != i && arr[pos] == min + pos * diff) {
                return false;
            }
            else if (pos != i){
                int temp = arr[pos];
                arr[pos] = arr[i];
                arr[i] = temp;
            }
            else {
                i++;
            }
        }
        return true;
    }
}