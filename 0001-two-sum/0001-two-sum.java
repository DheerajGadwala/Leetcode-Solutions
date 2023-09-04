class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int y = target - x;
            if (map.containsKey(y)) {
                return new int[] {i, map.get(y)};
            }
            else {
                map.put(x, i);
            }
        }
        return null;
    }
}