class Solution {
    public int minimumAverageDifference(int[] nums) {
        long rs_neg = 0, n = nums.length;
        for (int i: nums) rs_neg += i;
        long ans = Long.MAX_VALUE;
        int ans_arg = Integer.MAX_VALUE;
        long rs = 0;
        for (int i = 0; i < n; i++) {
            rs += nums[i];
            rs_neg -= nums[i];
            long l = rs  / (i + 1) ;
            long r = n - i - 1 == 0 ? 0 : rs_neg / (n - i - 1) ;
            if (Math.abs(l-r) < ans) {
                ans = Math.abs(l - r);
                ans_arg = i;
                
            }
        }
        return ans_arg;
    
    }
}