class Solution {
    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {
        List<List<Integer>> ans = new ArrayList<>();
        int n = nums.length;
        if (n == 0) {
            ans.add(Arrays.asList(lower, upper));
            return ans;
        }
        if (nums[0] != lower)
            ans.add(Arrays.asList(lower,nums[0] - 1));
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] + 1 != nums[i+1])
                ans.add(Arrays.asList(nums[i]+1, nums[i+1]-1));
        }
        if (nums[n-1] != upper)
            ans.add(Arrays.asList(nums[n-1]+1, upper));
        return ans;
    }
}