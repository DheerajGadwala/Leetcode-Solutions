class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer>[] mem = new HashMap[n];
        for (int i = 0; i < n; i++) {
            mem[i] = new HashMap<>();
        }
        int ans = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = nums[i] - nums[j];
                if (mem[j].containsKey(diff)) {
                    mem[i].put(diff, mem[j].get(diff) + 1);
                    ans = Math.max(ans, mem[i].get(diff));
                }
                else {
                    mem[j].put(diff, 1);
                    mem[i].put(diff, 2);
                }
            }
        }
        return ans;
    }
}