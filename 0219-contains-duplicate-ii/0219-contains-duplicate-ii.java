class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            if (!pos.containsKey(n)) pos.put(n, i);
            else if (i - pos.get(n) <= k) return true;
            else pos.put(n, i);
        }
        return false;
    }
}