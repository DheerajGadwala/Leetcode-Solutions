class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        Integer[] pos = new Integer[n];
        for (int i = 0; i < n; i++) pos[i] = i;
        Arrays.sort(pos, (a, b) -> Integer.compare(nums[a], nums[b]));
        int i = 0, j = n - 1;
        while (i < j) {
            if (nums[pos[i]] + nums[pos[j]] > target) j--;
            else if (nums[pos[i]] + nums[pos[j]] < target) i++;
            else return new int[] {pos[i], pos[j]};
        }
        return null;
    }
}