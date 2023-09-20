class Solution {
    
    public int minOperations(int[] nums, int x) {
        int sum = 0;
        for (int i: nums) {
            sum+=i;
        }
        int target = sum - x;
        int ans = target != 0 ? -1 : 0;
        int w = 0, i = 0, j = 0;
        
        if (target < 0) {
            return -1;
        }
        
        while (j < nums.length || w > target) {
            if (i == j) {
                w += nums[j];
                j++;
            }
            else if (w < target) {
                w += nums[j];
                j++;
            }
            else {
                w -= nums[i];
                i++;
            }
            if (w == target) {
                ans = Math.max(ans, j - i);
            }
        }
        
        return ans == -1 ? -1 : nums.length-ans;
    }
}