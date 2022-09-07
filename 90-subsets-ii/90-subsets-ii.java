class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> ret = new HashSet<>();
        ret.add(new ArrayList<>());
        for (int i = 0; i < nums.length; i++) {
            Set<List<Integer>> curr = new HashSet<>();
            for (List<Integer> l: ret) {
                List<Integer> copy = new ArrayList<>(l);
                copy.add(nums[i]);
                curr.add(copy);
            }
            ret.addAll(curr);
        }
        return new ArrayList<>(ret);
    }
}