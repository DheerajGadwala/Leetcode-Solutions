class Solution {
    
    Map<Integer, Integer>[] dp;
    int[] nums, multipliers;
    int n, m;
    
    public int maximumScore(int[] nums, int[] multipliers) {
        this.n = nums.length;
        this.m = multipliers.length;
        this.multipliers = multipliers;
        this.nums = nums;
        this.dp = new HashMap[n];
        return res(0, n-1);
    }
    
    private int res(int l, int r) {
        int i = n - 1 - r + l;
        if (dp[l] == null) dp[l] = new HashMap<>();
        if (dp[l].containsKey(r)) {
            return dp[l].get(r);
        }
        else if (i == m) {
            return 0;
        }
        else if (l == r) {
            dp[l].put(r, nums[l] * multipliers[i]);
            return dp[l].get(r);
        }
        else {
            dp[l].put(r, Math.max(nums[l] * multipliers[i] + res(l+1, r), nums[r] * multipliers[i] + res(l, r-1)));
            return dp[l].get(r);
        }
    }
}