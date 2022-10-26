class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int rs = 0, n = nums.length;
        Map<Integer, Integer> fo = new HashMap<>();
        fo.put(0, -1);
        for (int j = 0; j < n; j++) {
            int i = nums[j];
            rs += i;
            rs %= k;
            if (!fo.containsKey(rs)) fo.put(rs, j);
            else if (j - fo.get(rs) >= 2) return true;
        }
        return false;
    }
}