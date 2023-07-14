class Solution {
    public int longestSubsequence(int[] arr, int diff) {
        Map<Integer, Integer> prev = new HashMap<>();
        int ans = 1;
        for (int i: arr) {
            if (prev.containsKey(i - diff)) {
                prev.put(i, prev.get(i - diff) + 1);
                ans = Math.max(ans, prev.get(i));
            }
            else {
                prev.put(i, 1);
            }
        }
        return ans;
    }
}