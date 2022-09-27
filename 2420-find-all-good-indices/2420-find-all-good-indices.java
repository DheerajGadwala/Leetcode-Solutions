class Solution {
    public List<Integer> goodIndices(int[] nums, int k) {
        int before = 0, after = 0, n = nums.length;
        List<Integer> ans = new ArrayList<>();
        if (n < 2*k+1) return ans;
        for (int i = 1; i < k; i++) {
            // System.out.println(i + " " + (nums[i] > nums[i-1]));
            if (nums[i] > nums[i-1]) {
                before++;
            }
        }
        // System.out.println();
        for (int i = k + 2; i < 2 * k + 1; i++) {
            // System.out.println(i + " " + (nums[i] < nums[i-1]));
            if (nums[i] < nums[i-1]) {
                after++;
            }
        }
        for (int i = k; i < n - k; i++) {
            if (before == 0 && after == 0) {
                ans.add(i);
            }
            // System.out.println(i + " " + nums[i] + " " + before + " " + after);
            if (nums[i] > nums[i-1]) before++;
            if (nums[i-k+1] > nums[i-k]) before--;
            if (i != n-k-1 && nums[i+2] < nums[i+1]) after--;
            if (i != n-k-1 && nums[i+k+1] < nums[i+k]) after++;
        }
        return ans;
    }
}