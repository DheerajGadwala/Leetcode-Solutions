class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        Integer[][] mem = new Integer[n][1001];
        int ans = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = nums[i] - nums[j] + 500;
                if (mem[j][diff] != null) {
                    mem[i][diff] = mem[j][diff] + 1;
                    ans = Math.max(ans, mem[i][diff]);
                }
                else {
                    mem[j][diff] = 1;
                    mem[i][diff] = 2;
                }
            }
        }
        return ans;
    }
}