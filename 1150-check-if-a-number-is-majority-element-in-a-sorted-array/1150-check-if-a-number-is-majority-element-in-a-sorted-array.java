class Solution {
    
    public boolean isMajorityElement(int[] nums, int target) {
        int c = ceil(nums, target), f = floor(nums, target);
        return c - f + 1 > nums.length / 2;
    }
    
    private int ceil(int[] nums, int val) {
        int l = 0, h = nums.length - 1;
        int ans = -1;
        while (l <= h) {
            int m = (l + h) / 2;
            if (nums[m] == val) {
                ans = m;
            }
            if (nums[m] <= val) {
                l = m + 1;
            }
            else {
                h = m - 1;
            }
        }
        return ans;
    }
    
    private int floor(int[] nums, int val) {
        int l = 0, h = nums.length - 1;
        int ans = nums.length;
        while (l <= h) {
            int m = (l + h) / 2;
            if (nums[m] == val) {
                ans = m;
            }
            if (nums[m] >= val) {
                h = m - 1;
            }
            else {
                l = m + 1;
            }
        }
        return ans;
    }
}