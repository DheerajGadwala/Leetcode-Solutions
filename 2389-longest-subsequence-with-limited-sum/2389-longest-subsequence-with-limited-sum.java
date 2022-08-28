class Solution {
    int[] nums;
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i-1];
        }
        this.nums = nums;
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            ans[i] = search(queries[i]);
        }
        return ans;
    }
    
    private int search(int tar) {
        int n = nums.length;
        int l = 0, h = n - 1;
        while (l <= h) {
            int m = (l + h) / 2;
            int val = nums[m];
            if (val == tar) {
                return m + 1;
            }
            else if (val < tar) {
                l = m + 1;
            }
            else {
                h = m - 1;
            }
        }
        return l;
    }
}