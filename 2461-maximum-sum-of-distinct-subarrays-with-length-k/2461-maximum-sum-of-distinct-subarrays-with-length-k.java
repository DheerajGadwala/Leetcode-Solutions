class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long ans = 0, curr = 0;
        Map<Integer, Integer> window = new HashMap<>();
        for (int i = 0; i < k - 1; i++) {
            window.put(nums[i], window.getOrDefault(nums[i], 0) + 1);
            curr += nums[i];
        }
        for (int i = k - 1; i < n; i++) {
            window.put(nums[i], window.getOrDefault(nums[i], 0) + 1);
            curr += nums[i];
            if (window.size() == k && curr > ans) ans = curr;
            curr -= nums[i - k + 1];
            window.put(nums[i - k + 1], window.getOrDefault(nums[i - k + 1], 0) - 1);
            if (window.get(nums[i - k + 1]) == 0) window.remove(nums[i - k + 1]);
        }
        return ans;
    }
}