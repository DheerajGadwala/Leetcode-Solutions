class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int sum = 0, n = queries.length;
        int[] ans = new int[n];
        for (int k: nums) {
            if (k % 2 == 0) sum += k;
        }
        for (int i = 0; i < n; i++) {
            int[] q = queries[i];
            if (nums[q[1]] % 2 == 0) sum -= nums[q[1]];
            nums[q[1]] += q[0];
            if (nums[q[1]] % 2 == 0) sum += nums[q[1]];
            ans[i] = sum;
        }
        return ans;
    }
}