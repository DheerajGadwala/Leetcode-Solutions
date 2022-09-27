class Solution {
    public int longestSubarray(int[] nums) {
        int curr = 1, ans = 1, max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1]) {
                curr += 1;
                if (nums[i] == max)
                    ans = Math.max(ans, curr);
            }
            else if (nums[i] > max){
                max = nums[i];
                curr = 1;
                ans = 1;
            }
            else {
                curr = 1;
            }
        }
        return ans;
    }
}