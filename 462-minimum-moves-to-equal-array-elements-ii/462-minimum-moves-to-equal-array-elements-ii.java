class Solution {

    public int minMoves2(int[] nums) {
        int median = quickSelect(nums, 0, nums.length-1);
        int ans = 0;
        for (int k: nums) {
            ans += Math.abs(median - k);
        }
        return ans;
    }
    
    public int quickSelect(int[] nums, int i, int j) {
        if (i == j) {
            return nums[i];
        }
        int p = i, k = ++i;
        while (k <= j) {
            if (nums[k] < nums[p]) {
                int temp = nums[i];
                nums[i] = nums[k];
                nums[k] = temp;
                i++;k++;
            }
            else {
                k++;
            }
        }
        int temp = nums[p];
        nums[p] = nums[i-1];
        nums[i-1] = temp;
        if (i-1 == nums.length / 2) {
            return nums[i-1];
        } 
        else if (i-1 < nums.length / 2) {
            return quickSelect(nums, i, j);
        }
        else {
            return quickSelect(nums, p, i-2);
        }
    }
}