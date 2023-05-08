class Solution {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int i = 0, j = nums.length - 1;
        long ans = 0;
        int mod = (int)(Math.pow(10, 9)) + 7;
        int[] powers = new int[nums.length];
        powers[0] = 1;
        for (int k = 1; k < nums.length; k++)
            powers[k] = (powers[k - 1] * 2) % mod;
        while (i <= j) {
            if (nums[i] + nums[j] > target) {
                j--;
            }
            else {
                // System.out.println(ans + " " + i + " " + j);
                ans += powers[j - i];
                ans %= mod;
                i++;
            }
        }
        return (int) ans;
    }
}