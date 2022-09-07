class Solution {
    public int longestNiceSubarray(int[] nums) {
        int i = 0, j = 0, curr = 0, n = nums.length, ans = 0;
        while (j < n) {
            if ((curr & nums[j]) == 0) {
                curr |= nums[j++];
                ans = Math.max(ans, j-i);
            }
            else {
                curr ^= nums[i++];
            }
        }
        return ans;
    }
}