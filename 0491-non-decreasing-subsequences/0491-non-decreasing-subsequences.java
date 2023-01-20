class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        int n = nums.length;
        List<List<Integer>> ret = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int m = ret.size();
            for (int j = 0; j < m; j++) {
                List<Integer> l = ret.get(j);
                if (l.get(l.size()-1) <= nums[i]) {
                    List<Integer> copy = new ArrayList<>(l);
                    copy.add(nums[i]);
                    ret.add(copy);
                }
            }
            for (int j = 0; j < i; j++) {
                if (nums[j] <= nums[i]) {
                    List<Integer> l = new ArrayList<>();
                    l.add(nums[j]);
                    l.add(nums[i]);
                    ret.add(l);
                }
            }
        }
        return new ArrayList<>(new HashSet<>(ret));
    }
}