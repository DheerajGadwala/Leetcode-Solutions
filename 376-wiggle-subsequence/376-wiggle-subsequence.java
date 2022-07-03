class Solution {
    int[] nums;
    public int wiggleMaxLength(int[] nums) {
        this.nums = nums;
        return Math.max(res(0, 1, true), res(0, 1, false));
    }
    
    public int res(int prev, int pos, boolean inc) {
        if (pos == nums.length) {
            return 1;
        }
        else if (inc && nums[pos] > nums[prev]) {
            return 1 + res(pos, pos + 1, !inc);
        }
        else if (inc && nums[pos] <= nums[prev]) {
            return res(pos, pos+1, inc);
        }
        else if (!inc && nums[pos] < nums[prev]) {
            return 1 + res(pos, pos + 1, !inc);
        }
        else { // !inc && nums[pos] >= nums[prev]
            return res(pos, pos + 1, inc);
        }
    }
    
}