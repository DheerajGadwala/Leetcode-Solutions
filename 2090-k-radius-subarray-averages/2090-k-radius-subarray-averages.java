class Solution {
    public int[] getAverages(int[] nums, int k) {
        int n = nums.length;
        int[] ret = new int[n];
        for (int i = 0; i < k && i < n; i++) {
            ret[i] = -1;
            ret[n - 1 - i] = -1;
        }
        long j = 0;
        for (int i = 0; i < 2 * k + 1; i++) {
            if (i < n)
                j += nums[i];
        }
        if (k < n && k < n - k)
            ret[k] = (int) (j / (2 * k + 1));
        for (int i = k; i < n - k - 1; i++) {
            j -= nums[i - k];
            j += nums[i + k + 1];
            ret[i+1] = (int) (j / (2 * k + 1));
        }
        return ret;
    }
}