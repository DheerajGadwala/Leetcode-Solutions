class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ret = new ArrayList<>();
        if (nums.length == 0) {
            return ret;
        }
        int u = nums[0], v = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - 1 == nums[i-1]) {
                v = nums[i];
            }
            else {
                if (u != v)
                    ret.add(u + "->" + v);
                else
                    ret.add(""+u);
                u = nums[i];
                v = nums[i];
            }
        }
        if (u != v)
            ret.add(u + "->" + v);
        else
            ret.add(""+u);
        return ret;
    }
}